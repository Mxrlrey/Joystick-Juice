from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from .models import User
from . import forms
from django.urls import reverse_lazy


# Create your views here.
class UserRegisterView(CreateView):
    model = User
    form_class = forms.UserForm
    template_name = 'user_form.html' 
    success_url = reverse_lazy('user_list') 

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

class UpdateBioView(UpdateView):
    model= User
    fields = ['bio']
    template_name = 'user_bio.html'

    def get_success_url(self): 
        return reverse_lazy('user_profile', kwargs={'pk': self.object.pk})

class PerfilUserView(DetailView):
    model= User
    template_name = 'user_profile.html'