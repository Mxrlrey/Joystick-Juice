from django.urls import path
from . import views
from .views import RegisterView, UserListView, UserDeleteView


urlpatterns = [
    # /url no browser; a função resposável; nome da url
    path('register/', RegisterView.as_view(), name='user_register'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]