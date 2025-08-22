from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from .models import User
from Games.models import UserGameList
from Reviews.models import Review, Comment
from . import forms
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator



# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            return redirect("user_profile", pk=user.pk)
    else:
        form = forms.RegisterForm()
    return render(request, "user_register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("user_profile", pk=user.pk)
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return render(request, "user_login.html")

class LogoutUserView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('user_login')
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for user in context['users']:
            user.update_form = forms.UserFormUpdate(instance=user)
        return context


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = forms.UserFormUpdate
    
    def get_success_url(self): 
        return reverse_lazy('user_profile', kwargs={'pk': self.object.pk})

@method_decorator(never_cache, name='dispatch')
class UpdateBioView(LoginRequiredMixin, UpdateView):
    model= User
    fields = ['bio']
    login_url = reverse_lazy('user_login')

    def get_success_url(self): 
        return reverse_lazy('user_profile', kwargs={'pk': self.object.pk})

@method_decorator(never_cache, name='dispatch')
class PerfilUserView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_profile.html'
    login_url = reverse_lazy('user_login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_form'] = forms.UserFormUpdate(instance=self.object)
        context['bio_form'] = forms.UserFormBio(instance=self.object)
        context['reviews_count'] = Review.objects.filter(user=self.object).count()
        context['comments_count'] = Comment.objects.filter(user=self.object).count()

        game_list = UserGameList.objects.filter(user=self.object)
        context['stats'] = {
            "para_jogar": game_list.filter(status="P").count(),
            "jogando": game_list.filter(status="J").count(),
            "concluido": game_list.filter(status="C").count(),
            "abandonado": game_list.filter(status="A").count(),
            "total": game_list.count(),
        }

        return context
    
@login_required
def user_game_list(request, pk, status):
    user = User.objects.get(pk=pk)

    if status == "J":
        jogos = UserGameList.objects.filter(user=user, status="J")
        titulo = "Jogando"
    elif status == "C":
        jogos = UserGameList.objects.filter(user=user, status="C")
        titulo = "Concluídos"
    elif status == "A":
        jogos = UserGameList.objects.filter(user=user, status="A")
        titulo = "Abandonados"
    elif status == "P":
        jogos = UserGameList.objects.filter(user=user, status="P")
        titulo = "Para Jogar"
    elif status == "T":
        jogos = UserGameList.objects.filter(user=user)
        titulo = "Todos os Jogos"
    else:
        jogos = UserGameList.objects.none()
        titulo = "Desconhecido"

    return render(request, "user_game_list.html", {
        "user_profile": user,
        "jogos": jogos,
        "titulo": titulo
    })


@login_required
def user_reviews(request, pk):
    user = User.objects.get(pk=pk)
    reviews = Review.objects.filter(user=user)
    return render(request, "user_reviews.html", {
        "user_profile": user,
        "reviews": reviews
    })


@login_required
def user_comments(request, pk):
    user = User.objects.get(pk=pk)
    comments = Comment.objects.filter(user=user)
    return render(request, "user_comments.html", {
        "user_profile": user,
        "comments": comments
    })


