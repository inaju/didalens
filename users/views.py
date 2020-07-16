from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import CreateView
# Create your views here.

class Signup(CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name='signup.html'
