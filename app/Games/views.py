from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Render the home page of the Joystick Juice application.
    """
    return render(request, 'home.html')