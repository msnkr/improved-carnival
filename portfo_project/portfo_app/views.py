import os
from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import TemplateView
from .forms import ContactPageForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'portfo_app/home-page.html'


class AboutMeView(TemplateView):
    template_name = 'portfo_app/about-me.html'


class ExperienceView(TemplateView):
    template_name = 'portfo_app/experience.html'


class ProjectsView(TemplateView):
    template_name = 'portfo_app/projects.html'


def ContactPageView(request):
    form = ContactPageForm()
    if request.method == 'POST':
        form = ContactPageForm(request.POST)
        if form.is_valid():
            email_message = form.cleaned_data['message']
            form_email = form.cleaned_data['email']
            form_name = form.cleaned_data['name']
            form_form = f'Message: {email_message} \n\n From: {form_email} \n\n Name: {form_name}'
            send_mail('New Message From Website', form_form, os.getenv('EMAIL_USER'), [os.getenv('TO_USER')])
            return thank_you(request)
        else:
            return ValidationError('Error')
    else:
        return render(request, 'portfo_app/contact-me.html', {'form': form})


def thank_you(request):
    return render(request, 'portfo_app/thank-you.html')


def error404(request, exception):
    return render(request, 'portfo_app/error404.html')


def error500(request):
    return render(request, 'portfo_app/error500.html')