from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['opinion']
        widgets = {
            'opinion': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Escreva seu comentário...'
            })
        }