from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.
def send_email(user, subject, template, data={}):
    html_body = render_to_string(template, {'user':user, 'data':data})
    msg = EmailMultiAlternatives(subject, '', to=[user.email])
    msg.attach_alternative(html_body, 'text/html')
    msg.send()