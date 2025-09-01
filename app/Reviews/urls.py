from django.urls import path
from . import views

urlpatterns = [
    path('review/<int:review_id>/comment/', views.add_comment, name="add_comment"),
]