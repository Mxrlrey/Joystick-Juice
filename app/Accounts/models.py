from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100, verbose_name="Nome Completo")
    birthdate = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")
    gender = models.CharField(
        max_length=1,
        choices=[
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('O', 'Outro'),
        ],
        null=True,
        blank=True,
        verbose_name="Gênero"
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True, verbose_name="Biografia")

    def save(self, *args, **kwargs):
        if self.pk:
            old = User.objects.filter(pk=self.pk).first()
            if old and old.avatar and old.avatar != self.avatar:
                old.avatar.delete(save=False)
        super().save(*args, **kwargs)
