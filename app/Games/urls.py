from django.urls import path
from . import views


urlpatterns = [
    # /url no browser; a função resposável; nome da url
    path('home/', views.home, name='home'),
    path('listar/', views.listar_jogos, name='listar_jogos'),
    path('preencher/', views.preencher_e_salvar, name='preencher_e_salvar'),
    path('games/<int:pk>/', views.Games.as_view(), name='games'),
    path('games/<int:game_id>/add/', views.add_to_list, name='add_to_list'),
    path('games/<int:game_id>/update-status/', views.update_game_status, name='update_game_status'),
    path('games/<int:game_id>/remove/', views.remove_from_list, name='remove_from_list'),
]
