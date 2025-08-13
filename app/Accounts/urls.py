from django.urls import path
from . import views



urlpatterns = [
    # /url no browser; a função resposável; nome da url
    path('register/', views.register_view, name='user_register'),
    path('login/', views.login_view, name='user_login'),
    path('logout/', views.LogoutUserView.as_view(), name='user_logout'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),
    path('bio/<int:pk>/', views.UpdateBioView.as_view(), name='user_bio'),
    path('profile/<int:pk>/', views.PerfilUserView.as_view(), name="user_profile")

]