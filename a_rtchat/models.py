from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class ChatGroup(models.Model):
    group_name = models.CharField( max_length=125, unique=True)
    users_name = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='online_in_groups', blank=True)
    def __str__(self):
        return self.group_name
    

class Groupmessage(models.Model):
    group = models.ForeignKey(ChatGroup, related_name='chat_messages', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.author.username} : {self.body}'
    
    class Meta:
        ordering = ['-created']




    
    