from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=[
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('O', 'Outro'),
        ],
        null=True,
        blank=True
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:
            old = User.objects.filter(pk=self.pk).first()
            if old and old.avatar and old.avatar != self.avatar:
                old.avatar.delete(save=False)
        super().save(*args, **kwargs)
