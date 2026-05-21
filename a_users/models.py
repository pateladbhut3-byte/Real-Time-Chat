from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    blocked_users = models.ManyToManyField('self', symmetrical=False, related_name='blocked_by', blank=True)

    def __str__(self):
        return self.username
    
    def block(self, user):
        if user != self:
            self.blocked_users.add(user)

    def unblock(self, user):
        if user != self:
            self.blocked_users.remove(user)

    def is_blocked_by(self, user):
        return self in user.blocked_users.all()

    def is_blocking(self, user):
        return self.blocked_users.filter(id=user.id).exists()

    @property
    def name(self):
        if self.displayname:
            name = self.displayname
        else:
            name = self.username 
        return name
    
    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except:
            avatar = static('images/avatar.svg')
        return avatar
