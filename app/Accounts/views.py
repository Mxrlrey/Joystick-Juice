from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from .models import User
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

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = forms.UserFormUpdate
    template_name = 'user_update.html'
    success_url = reverse_lazy('user_list')

@method_decorator(never_cache, name='dispatch')
class UpdateBioView(LoginRequiredMixin, UpdateView):
    model= User
    fields = ['bio']
    template_name = 'user_bio.html'
    login_url = reverse_lazy('user_login')


    def get_success_url(self): 
        return reverse_lazy('user_profile', kwargs={'pk': self.object.pk})

@method_decorator(never_cache, name='dispatch')
class PerfilUserView(LoginRequiredMixin, DetailView):
    model= User
    template_name = 'user_profile.html'
    login_url = reverse_lazy('user_login')



