from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'portfo_app/home-page.html')


def about_me(request):
    return render(request, 'portfo_app/about-me.html')