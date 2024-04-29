from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class LandingView(TemplateView):
    template_name = "pages/landing.html"

class AboutView(TemplateView):
    template_name = "pages/about.html"

class ProjectsView(TemplateView):
    template_name = "pages/projects.html"

class ContactView(TemplateView):
    template_name = "pages/contact.html"