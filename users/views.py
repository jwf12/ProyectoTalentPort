from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from django.contrib.auth.hashers import make_password

from .models import FriendList, User
from .serializers import FriendListSerializer, UserSerializer
import jwt, datetime


# USER LOGIN REGISTER LOG OUT GET UPDATE
class RegisterApiView(APIView):
    """
    This endpoint creates a new user.

    - Request:
        - name (string): First name for de new user.
        - username (string): The username for the new user.
        - mail (string): The email address for the new user.
        - password (string): The password for the new user.

    - Response:
        - 201 Created: The user was successfully created.
        - 400 Bad Request: If the username or email already exist or if not all fields are provided.
    """
    def post(self, request):
        data = request.data
        username = data.get('username')
        mail = data.get('mail')
        password = data.get('password')
        
        if password:
            data['password'] = make_password(password)

        serialiazer = UserSerializer(data=data)

        if serialiazer.is_valid():
            serialiazer.save()
            return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)
        
        else:
            if User.objects.filter(username=username):#User validation, unique=True
                return Response({'Error': 'Username already exist'}, status=status.HTTP_400_BAD_REQUEST)
            
            if User.objects.filter(email=mail):#Mail validation, unique=True
                return Response({'error': 'Email already exist'}, status=status.HTTP_400_BAD_REQUEST)                
            
            return Response({'error': serialiazer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(APIView):
    """
        This endpoint logs in a user and returns a JWT token.

        - Request:
            - username (string): The username of the user.
            - password (string): The password of the user.

        - Response:
            - 200 OK: Successful login. Returns a JWT token in the response.
            - 400 Bad Request: If the username is not found or the password is incorrect.
    """
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username).first() 

        if user is None:
            return Response({'Error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not user.check_password(password):
            return Response({'Error': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)
        
        payload={
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data={'jwt': token}

        return response
    

class EditUserApiView(APIView):
    """
        This endpoint allows a user to edit their own information.

        - Method: PUT
        - Request:
            - All fields required except password.

        - Response:
            - 200 OK: User information updated successfully.
            - 400 Bad Request: If the user is not found or there are validation errors.
    """
    def put(self, request):
        token = request.COOKIES.get('jwt') #traemos el usuario con las cookies
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        object = User.objects.get(id= payload['id'])#Traemos el objeto

        if object:#Validamos

            password = request.data.get('password')
            if password:
                request.data['password'] = make_password(password)
            else:
                # Si no se proporciona una nueva contraseña, conservamos la contraseña existente
                request.data['password'] = object.password

            object_serilize = UserSerializer(object, data=request.data)#Serializamos el objeto y la actualizacion
            if object_serilize.is_valid():#Validamos

                object_serilize.save()
                return Response({'message': 'Updated'}, status=status.HTTP_200_OK)
            
            return Response({'error': 'All fields required'}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)


class UserGetViewAPIView(APIView):
    """
    This endpoint retrieves information about the authenticated user.

    - Method: GET
    - Request:
        - Requires a valid JWT token in the request cookies for authentication.

    - Response:
        - 200 OK: Returns information about the authenticated user.
        - 401 Unauthorized: If the request does not include a valid JWT token or the token is expired.
    """
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        user_serialize = UserSerializer(user)

        return Response(user_serialize.data)


class LogoutApiView(APIView):
    """
    This endpoint logs out the user by deleting the JWT token cookie.

    - Method: POST
    - Request:
        - No request parameters required.

    - Response:
        - 200 OK: Logout successful. Deletes the JWT token cookie.
    """
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data={
            'Message': 'Logout succesfully'
        }
        return response

    
#USER FRIANDLIST

class FriendAdd(generics.CreateAPIView):
    model = FriendList
    serializer_class = FriendListSerializer

class FriendListView(generics.ListAPIView):
    model = FriendList
    serializer_class = FriendListSerializer

    def get_queryset(self):
        user = self.request.user
        return FriendList.objects.filter(userlist=user)