from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .forms import CommentForm

@login_required
def add_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
            return redirect('review_detail', pk=review.pk)  # Ajuste para sua rota de detalhe da review
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'review': review})
