from django.urls import path
from . import views

urlpatterns = [
    # /url no browser; a função resposável; nome da url
    path('home/', views.home, name='home'),
    path('listar/', views.listar_jogos, name='listar_jogos'),
    path('preencher/', views.preencher_e_salvar, name='preencher_e_salvar'),
    path('games/<int:pk>/', views.games.as_view(), name='games'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
]