from django.urls import path
from . import views

urlpatterns = [
    # /url no browser; a função resposável; nome da url
    path('home/', views.home, name='home'),
]