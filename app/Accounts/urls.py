from django.urls import path
from . import views  # views do Accounts
from Games.views import UserGameListView


urlpatterns = [
    path('register/', views.register_view, name='user_register'),
    path('login/', views.login_view, name='user_login'),
    path('logout/', views.LogoutUserView.as_view(), name='user_logout'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('bio/<int:pk>/', views.UpdateBioView.as_view(), name='user_bio'),
    path('profile/<int:pk>/', views.PerfilUserView.as_view(), name="user_profile"),
    path('profile/<int:pk>/reviews/', views.user_reviews, name="user_reviews"),
    path('profile/<int:pk>/comments/', views.user_comments, name="user_comments"),
    path('profile/<int:pk>/games/', UserGameListView.as_view(), name="user_game_list"),
    path('profile/<int:pk>/games/<str:status>/', UserGameListView.as_view(), name="user_game_list_by_status"),
]
