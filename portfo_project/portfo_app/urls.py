from django.urls import path
from .views import home_page, about_me

urlpatterns = [
    path('', home_page, name='home-page'),
    path('about-me', about_me, name='about'),
]