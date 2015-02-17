from django.shortcuts import render
from TasksManager.models import Supervisor
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
def page(request):
    if request.POST:
        form = Form_supervisor(request.POST)
        if form.is_valid():
        name = form.cleaned_data['name']
        login = form.cleaned_data['login']
        password = form.cleaned_data['password']
        specialisation = form.cleaned_data['specialisation']
        email = form.cleaned_data['email']
        new_user = User.objects.create_user(username = login, email = email, password=password)
        new_user.is_active = True
        new_user.last_name=name
        new_user.save()
        new_supervisor = Supervisor(user_auth = new_user, specialisation=specialisation)
        new_supervisor.save()
        return HttpResponseRedirect(reverse('public_empty'))
    else:
        return render(request, 'en/public/create_supervisor.html', {'form' : form})

