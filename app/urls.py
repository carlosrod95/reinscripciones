
from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from .views import GeneratePdf


from django.views.generic import View

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('imprimir/', views.imprimir, name='imprimir'),

    path('pdf/', GeneratePdf.as_view()),




    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    

]
