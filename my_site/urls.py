from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('signin', views.UserFormView.as_view(), name='signin'),
    path('retrieve1', views.retrieve1, name='retrieve1'),
    #path('retrieve2', views.retrieve2, name='retrieve2'),
    #path('signup2', views.abc.as_view(), name='signup2'),
]
