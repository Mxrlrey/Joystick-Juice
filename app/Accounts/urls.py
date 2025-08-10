from django.urls import path
from . import views
from .views import RegisterView, UserListView, UserDeleteView, UserUpdateView


urlpatterns = [
    # /url no browser; a função resposável; nome da url
    path('register/', RegisterView.as_view(), name='user_register'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]