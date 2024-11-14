from django.shortcuts import render,redirect
import requests
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import *
from .forms import CustomUserLoginForm

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomPasswordChangeForm
import json

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#Page d'acceuil
def home(request):
    return render(request, 'app/acceuil.html')

#Creation de compte utilisateur 

def inscription(request):
     if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre compte a été créé avec succès")
            return redirect('connexion') 
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
     else:
        form = CustomUserCreationForm()
     return render(request, 'app/inscription.html',{'form':form})

# Authentification à la connexion 
def connexion(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Vous êtes connecté avec succès.")
                return redirect('tableaudebord')  # Rediriger vers une page après connexion
            else:
                messages.error(request, "Email ou mot de passe invalide.")
    else:
        form = CustomUserLoginForm() 

    return render(request, 'app/connexion.html',{'form': form})


def tableaudebord(request):
    user=request.user
    return render(request, 'app/tableaudebord.html',{'user':user})

def contact(request):
    return render(request, 'app/contact.html')

def profile(request):
    return render(request, 'app/profile')