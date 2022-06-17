from django.urls import path
from .views import HomePageView, ExperienceView, AboutMeView, ProjectsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('about-me', AboutMeView.as_view(), name='about'),
    path('projects', ProjectsView.as_view(), name='projects'),
    path('experience', ExperienceView.as_view(), name='experience'),
]