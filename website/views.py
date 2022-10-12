import email
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .models import EmailMessage
from .forms import ContactForm
# Create your views here.

class HomePageView(TemplateView):
    template_name= 'website/home.html'

class AboutPageView(TemplateView):
    template_name= 'website/about.html'

class BlogPageView(TemplateView):
    template_name= 'website/blog.html'

class ContactPageView(FormView):
    template_name= 'website/contact.html'
    form_class = ContactForm
    success_url = '/'
    
    def form_valid(self, form):
        email = form.cleaned_data['from_email']
        subj = form.cleaned_data['subject']
        msg = form.cleaned_data['message']
        
        try:
            send_mail(subj, msg, email, ['benjaminochieng99@gmail.com'])
            message = EmailMessage(email=email, subject=subj, body=msg)
            message.save()
            
        except BadHeaderError:
            return HttpResponse('Bad Header Error Found!')
        
        return super().form_valid(form)
            
# def home_page_view(request):
#     return HttpResponse('<h1>Welcome to my home page</h1>')

# def about_page_view(request):
#     return HttpResponse('<h1>Welcome to my about page</h1>')

# def contact_page_view(request):
#     return HttpResponse('<h1>Welcome to my contact page</h1>')