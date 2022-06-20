from django.urls import path, include
from .views import HomePageView, ExperienceView, AboutMeView, ProjectsView, ContactPageView, thank_you

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('about-me', AboutMeView.as_view(), name='about'),
    path('projects', ProjectsView.as_view(), name='projects'),
    path('experience', ExperienceView.as_view(), name='experience'),
    path('contact-me', ContactPageView, name='contact-me'),
    path('contact-me/thank-you', thank_you, name='thank-you'),
    path('captcha/', include('captcha.urls'), )
]