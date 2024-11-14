from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import UserProfile  # Assurez-vous que UserProfile est bien importé s'il est utilisé dans la validation
from django.contrib.auth.forms import PasswordChangeForm

class CustomUserCreationForm(UserCreationForm):
    nom= forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400', 'placeholder': 'Votre nom'}))
    prenom= forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400', 'placeholder': 'vos prénoms'}))
    email= forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400', 'placeholder': 'Votre email'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400', 'placeholder': 'Numéro de téléphone'}))
    npi= forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400', 'placeholder': 'NPI'}))
    code_postal=forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400', 'placeholder': 'Code postal'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400', 'placeholder': 'Mot de passe'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400', 'placeholder': 'Confirmation'}))

    class Meta:
        model = CustomUser
        fields = ('nom','prenom','email', 'telephone','npi','code_postal', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserProfile.objects.filter(email=email).exists():
            raise forms.ValidationError("Ce email existe déjà.")
        return email

class CustomUserLoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400',
            'placeholder': 'Email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-400',
            'placeholder': 'Mot de passe'
        })
    )






class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input w-full pl-10 py-2 border border-gray-300 rounded-lg focus:border-orange-500 focus:ring-2 focus:ring-orange-200',
            'placeholder': 'Ancien mot de passe'
        })
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input w-full pl-10 py-2 border border-gray-300 rounded-lg focus:border-orange-500 focus:ring-2 focus:ring-orange-200',
            'placeholder': 'Nouveau mot de passe'
        })
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input w-full pl-10 py-2 border border-gray-300 rounded-lg focus:border-orange-500 focus:ring-2 focus:ring-orange-200',
            'placeholder': 'Confirmer le mot de passe'
        })
    )


