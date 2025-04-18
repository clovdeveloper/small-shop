from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import (
    Article, Commande, Vente, Fournisseur,
    Client, Categorie, Employe, AppUser
)

# Custom AuthenticationForm with Bootstrap styling
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'date_expiration': forms.DateInput(attrs={'type': 'date'}),
            'date_fabrication': forms.DateInput(attrs={'type': 'date'}),
        }

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'
        widgets = {
            'date_commande': forms.DateInput(attrs={'type': 'date'}),
        }

class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['client','article','quantite','prix','date_vente']
        widgets = {
            'date_vente': forms.DateInput(attrs={'type': 'date'}),
        }

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'

class AppUserForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ['username', 'email', 'first_name', 'last_name', 'telephone', 'cni', 'adresse', 'role']
