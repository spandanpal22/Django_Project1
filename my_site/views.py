from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact,StudentData
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm


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

def signin(request):
    if request.method=='POST':
        email_r=request.POST.get('email')
        password_r=request.POST.get('password')

        return HttpResponse(email_r)

    else:
        return render(request,'my_site/signin.html')


def signup(request):
    if request.method=='POST':
        Fname=request.POST.get('firstName')
        Lname=request.POST.get('lastName')
        email_r = request.POST.get('email')
        un_r = request.POST.get('username')
        password_r = request.POST.get('password')

        d=StudentData(firstName=Fname,lastName=Lname ,email=email_r,username=un_r,password=password_r)
        d.save()

        return render(request, 'my_site/signup.html')
    else:
        return render(request,'my_site/signup.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'my_site/signin.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form = self.form_class(request.POST)


        if form.is_valid():

            user=form.save(commit=False)
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()


            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return HttpResponse(request.POST.get('username'))

        return render(request, self.template_name, {'form': form})

"""class abc(View):
    form_class = UserForm
    template_name = 'my_site/signup2.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form = self.form_class(request.POST)
        print('Hi')
        if form.is_valid():
            user = form.save(commit=False)

            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()



        return render(request, self.template_name, {'form': form})"""