"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages

from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from app.forms import UserForm,ProfileForm,CreaProfileFORM,SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect




from django.http import HttpResponse
from django.views.generic import View

#importing get_template from loader
from django.template.loader import get_template

#import render_to_pdf from util.py 
from .utils import render_to_pdf 

#Creating our view, it is a class based view
class GeneratePdf(View):


     def get(self, request, *args, **kwargs):
        #getting the template
        pdf = render_to_pdf('app/invoice.html')
         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

#class GeneratePdf(View):
    #def get(self, request, *args, **kwargs):
        #template = get_template('app/invoice.html')
        #context = {
            
        #}
        #html = template.render(context)
        #pdf = render_to_pdf('app/invoice.html', context)
        #if pdf:
            #response = HttpResponse(pdf, content_type='application/pdf')
            #filename = "Invoice_%s.pdf" %("12341231")
            #content = "inline; filename='%s'" %(filename)
            #download = request.GET.get("download")
            #if download:
                #content = "attachment; filename='%s'" %(filename)
            #response['Content-Disposition'] = content
            #return response
        #return HttpResponse("Not found")













@login_required
def imprimir(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/imprimir.html',
        {
            'title':'imprimir',
            'year':datetime.now().year,
        }
    )
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
@login_required
@transaction.atomic
def update_profile(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('/imprimir')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'app/registA.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'title':'request',
        'message':'Your application description page.',
         'year':datetime.now().year,
    })
def create_profile(request):
    assert isinstance(request, HttpRequest)
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'app/altacuenta.html', {
        'form': form,
        'title':'request',
        'message':'Your application description page.',
         'year':datetime.now().year,
    })

