from django.db import models

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
    password = models.CharField(max_length=128)  # Store hashed passwords  

class User(Person):
    nickname = models.CharField(max_length=45)
    bio = models.TextField(max_length=200)
    

class Moderator(Person):
    is_active = models.BooleanField(default=True)

