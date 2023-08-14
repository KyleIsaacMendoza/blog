# accounts/views.py
# todo: we need to import
# UserCreateForm for default fields to fill up on our form on signing up
# reverse_lazy - to redirect user to the login page upon succesful registration
# CreateView - always use upon creating a new data (contents, accounts, etc) to pass onto our ClassBased View

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    # next is to create the file signup.html inside templates/registration
