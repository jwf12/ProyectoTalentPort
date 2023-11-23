from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import status

from .models import Project, FriendList

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

# Vista o lógica de creación de proyectos
def create_project(request):
    current_user = request.user  # Suponiendo que has autenticado al usuario
    friends = FriendList.objects.filter(userlist=current_user)

    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            new_project = serializer.save(user_project=current_user)
            new_project.collaborators.set(friends)
            return Response({'message': 'Project created successfully'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)