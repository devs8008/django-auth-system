from django.views.generic import TemplateView
# This 3 import for signup view
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView



class HomePageView(TemplateView):
    template_name = "home.html"

class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

