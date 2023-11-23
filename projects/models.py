from django.db import models

from users.models import User, FriendList

class Project(models.Model):
    user_project = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)
    LENGUAGES_OPTIONS = (
        ('1', 'Js'),
        ('2', 'Python'),
        ('3', 'Java'),
        ('4', 'Rust'),
        ('5', 'Go')
    )
    lenguages1_project = models.CharField(max_length=20, choices=LENGUAGES_OPTIONS, null=True, blank=True)
    lenguages2_project = models.CharField(max_length=20, choices=LENGUAGES_OPTIONS, null=True, blank=True)
    collaborators = models.ManyToManyField(FriendList, related_name='collaborations', blank=True, null=True)
    project_url = models.URLField(max_length=200,blank=True, null=True)
    repo_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
