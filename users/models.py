from django.db import models
from django.contrib.auth.models import AbstractUser


   
class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=15, null=True, blank=True)
    mail = models.EmailField()
    profile_pic = models.ImageField(upload_to='static/img', blank=True, null=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    LENGUAGES_OPTIONS = (
        ('1', 'Js'),
        ('2', 'Python'),
        ('3', 'Java'),
        ('4', 'Rust'),
        ('5', 'Go')
    )
    lenguages1 = models.CharField(max_length=20, choices=LENGUAGES_OPTIONS, null=True, blank=True)
    lenguages2 = models.CharField(max_length=20, choices=LENGUAGES_OPTIONS, null=True, blank=True)
    STACK_OPTIONS = (
        ('1', 'Front-End'),
        ('2', 'Back-End'),
        ('3', 'Full-Stack')
    )
    stack = models.CharField(max_length=20, choices=STACK_OPTIONS, null=True, blank=True)
    open_work = models.BooleanField(default=True, null=True, blank=True)

    #User internal information
    creation_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.username
    

class FriendList(models.Model):
    userlist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userlist_set')
    friendlist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendlist_set')

    def __str__(self):
        return f'{self.friendlist.username}'