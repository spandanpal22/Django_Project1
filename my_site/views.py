from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'my_site/index.html')

def about(request):
    return render(request,'my_site/about.html')

def yt(request):
    return render(request,'www.youtube.com')