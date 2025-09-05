from django.db import models
from django.conf import settings


class Game(models.Model):
    gameID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)  
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    synopsis = models.TextField()
    developer = models.CharField(max_length=100)
    cover_url = models.URLField(max_length=200, blank=True, null=True)
    banner_url = models.URLField(max_length=200, blank=True, null=True)   # novo
    trailer_url = models.URLField(max_length=200, blank=True, null=True)

class UserGameList(models.Model):
    STATUS_CHOICES = [
        ('P', 'Para jogar'),
        ('J', 'Jogando'),
        ('C', 'Concluído'),
        ('A', 'Abandonado'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey('Games.Game', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    date_added = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'game')
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.user.username} - {self.game.title} ({self.get_status_display()})"

    

class FavoriteGames(models.Model):
    user = models.ForeignKey('Accounts.User', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

class LikeGame(models.Model):
    user = models.ForeignKey('Accounts.User', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

