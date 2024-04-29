from django.urls import path
from .views import *

urlpatterns = [
    path("", LandingView.as_view(), name="landing"),
    path("about", AboutView.as_view(), name="about"),
    path("projects", ProjectsView.as_view(), name="projects"),
    path("contact", ContactView.as_view(), name="contact"),
]