from django.db import models
import os
from django.conf import settings

class Person(models.Model):
    personID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ])
    password = models.CharField(max_length=128) 
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            old = User.objects.get(pk=self.pk)
        except User.DoesNotExist:
            old = None

        super().save(*args, **kwargs)
        
        if old and old.avatar and old.avatar != self.avatar:
            old_avatar_path = os.path.join(settings.MEDIA_ROOT, old.avatar.name)
            if os.path.isfile(old_avatar_path):
                os.remove(old_avatar_path)
    

class User(Person):
    nickname = models.CharField(max_length=45)
    bio = models.TextField(max_length=200, null=True, blank=True)
    

class Moderator(Person):
    is_active = models.BooleanField(default=True)

