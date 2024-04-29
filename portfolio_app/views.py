from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class LandingView(TemplateView):
    template_name = "pages/landing.html"

class AboutView(TemplateView):
    template_name = "pages/about.html"

class ProjectsView(TemplateView):
    template_name = "pages/projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        projects = [
            {'name': 'Estudev', 
             'desc': "Discover a collaborative network of student developers to elevate your development skills and tech career aspirations.",
             'imgLink': "https://baryshnikov.vercel.app/assets/estudev-4q2zFER-.png",
             'githubLink': 'https://github.com/raishudesu/eStudev'
            },
            {'name': 'Reverie', 
             'desc': "A web-based diary application that's accessible from both desktop and mobile browsers.",
             'imgLink': "https://baryshnikov.vercel.app/assets/reverie-pgd8GGzX.png",
             'githubLink': 'https://github.com/raishudesu/Reverie'
            },
            {'name': 'Quillify', 
             'desc': "Digital source for tech insights, tutorials, and community discussions.",
             'imgLink': "https://baryshnikov.vercel.app/assets/quillify-fYo-Eua6.png",
             'githubLink': 'https://github.com/raishudesu/quillify-client'
            },
        ]
        context['projects'] = projects
        return context

class ContactView(TemplateView):
    template_name = "pages/contact.html"