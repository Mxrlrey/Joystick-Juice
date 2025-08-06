from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    reviewID = models.AutoField(primary_key=True)
    review = models.TextField(max_length=4000)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    user = models.ForeignKey('Accounts.User', on_delete=models.CASCADE, related_name='reviews')
    game = models.ForeignKey('Games.Game', on_delete=models.CASCADE, related_name='reviews')

class likeReview(models.Model):
    user = models.ForeignKey('Accounts.User', on_delete=models.CASCADE, related_name='liked_reviews')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')
    
class Comment(models.Model):
    commentID = models.AutoField(primary_key=True)
    opnion = models.TextField(max_length=500)
    user = models.ForeignKey('Accounts.User', on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')

class likeComment(models.Model):
    user = models.ForeignKey('Accounts.User', on_delete=models.CASCADE, related_name='liked_comments')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')


