# accounts/urls.py
from django.urls import path  # needed
from .views import SignUpView  # CBV we will create inside view


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    # we put signup/ in url because over all it will look like
    # accounts/signup/, next go to our views and create the class-based view
]
