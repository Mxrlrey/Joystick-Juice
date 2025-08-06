from django.db import models

class User(models.Model):
    userID = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=45)
    bio = models.TextField(max_length=200)
