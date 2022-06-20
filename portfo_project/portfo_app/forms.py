from django import forms
from captcha.fields import CaptchaField

class ContactPageForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    message = forms.Textarea()
    captcha = CaptchaField()