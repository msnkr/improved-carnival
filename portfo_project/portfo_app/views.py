from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'portfo_app/home-page.html'


class AboutMeView(TemplateView):
    template_name = 'portfo_app/about-me.html'


class ExperienceView(TemplateView):
    template_name = 'portfo_app/experience.html'


class ProjectsView(TemplateView):
    template_name = 'portfo_app/projects.html'
