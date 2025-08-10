from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import User
from .forms import UserForm
from django.urls import reverse_lazy

# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserForm
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