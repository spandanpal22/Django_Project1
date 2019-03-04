from django.shortcuts import render
from .models import Contact
# Create your views here.

def index(request):
    return render(request,'my_site/index.html')

def about(request):
    return render(request,'my_site/about.html')

def contact(request):
    if request.method=='POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c=Contact(email=email_r,subject=subject_r,message=message_r)
        c.save()

        return render(request, 'my_site/contact.html')
    else:
        return render(request,'my_site/contact.html')