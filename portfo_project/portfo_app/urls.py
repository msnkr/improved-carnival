from django.urls import path
from .views import home_page, about_me, projects, experience

urlpatterns = [
    path('', home_page, name='home-page'),
    path('about-me', about_me, name='about'),
    path('projects', projects, name='projects'),
    path('experience', experience, name='experience'),
]