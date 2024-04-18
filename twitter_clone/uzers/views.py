from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreateionForm


class SignUp(CreateView):
    form_class = CreateionForm
    success_url = reverse_lazy('posts_app:first')
    template_name = 'users/signup.html'
