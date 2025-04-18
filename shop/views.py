from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import Article, Commande, Vente, Fournisseur, Client, Categorie, Employe, AppUser
from .forms import ArticleForm, CommandeForm, VenteForm, FournisseurForm, ClientForm, CategorieForm, EmployeForm, \
    AppUserForm, LoginForm
from .decorators import admin_required


# === ARTICLE ===
@login_required
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'shop/article_list.html', {'articles': articles})

@login_required
def article_create(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'shop/confirm_delete.html', {'object': article})


# === COMMANDE ===
@login_required
def commande_list(request):
    commandes = Commande.objects.all()
    return render(request, 'shop/commande_list.html', {'commandes': commandes})

@login_required
def commande_create(request):
    form = CommandeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('commande_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def commande_update(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    form = CommandeForm(request.POST or None, instance=commande)
    if form.is_valid():
        form.save()
        return redirect('commande_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def commande_delete(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('commande_list')
    return render(request, 'shop/confirm_delete.html', {'object': commande})


# === VENTE ===
@login_required
def vente_list(request):
    ventes = Vente.objects.all()
    return render(request, 'shop/vente_list.html', {'ventes': ventes})

from django.shortcuts import render, redirect
from .forms import VenteForm
from .models import Employe

@login_required
def vente_create(request):
    user = request.user
    try:
        employe = Employe.objects.get(user=user)
    except Employe.DoesNotExist:
        # Redirige ou affiche un message d'erreur si l'utilisateur n'est pas un employé
        return render(request, 'shop/unauthorized.html', status=403)

    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            vente = form.save(commit=False)
            vente.employe = employe
            vente.save()
            return redirect('vente_list')
    else:
        form = VenteForm()

    return render(request, 'shop/form.html', {'form': form})


@login_required
def vente_update(request, pk):
    vente = get_object_or_404(Vente, pk=pk)
    form = VenteForm(request.POST or None, instance=vente)
    if form.is_valid():
        form.save()
        return redirect('vente_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def vente_delete(request, pk):
    vente = get_object_or_404(Vente, pk=pk)
    if request.method == 'POST':
        vente.delete()
        return redirect('vente_list')
    return render(request, 'shop/confirm_delete.html', {'object': vente})


# === FOURNISSEUR ===
@login_required
def fournisseur_list(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'shop/fournisseur_list.html', {'fournisseurs': fournisseurs})

@login_required
def fournisseur_create(request):
    form = FournisseurForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fournisseur_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def fournisseur_update(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    form = FournisseurForm(request.POST or None, instance=fournisseur)
    if form.is_valid():
        form.save()
        return redirect('fournisseur_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def fournisseur_delete(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('fournisseur_list')
    return render(request, 'shop/confirm_delete.html', {'object': fournisseur})


# === CLIENT ===
@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'shop/client_list.html', {'clients': clients})

@login_required
def client_create(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'shop/confirm_delete.html', {'object': client})


# === CATEGORIE ===
@login_required
def categorie_list(request):
    categories = Categorie.objects.all()
    return render(request, 'shop/categorie_list.html', {'categories': categories})

@login_required
def categorie_create(request):
    form = CategorieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('categorie_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def categorie_update(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    form = CategorieForm(request.POST or None, instance=categorie)
    if form.is_valid():
        form.save()
        return redirect('categorie_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def categorie_delete(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('categorie_list')
    return render(request, 'shop/confirm_delete.html', {'object': categorie})


# === EMPLOYE ===
@login_required
def employe_list(request):
    employes = Employe.objects.all()
    return render(request, 'shop/employe_list.html', {'employes': employes})

@login_required
def employe_create(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employe_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def employe_update(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    form = EmployeForm(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        return redirect('employe_list')
    return render(request, 'shop/form.html', {'form': form})

@login_required
def employe_delete(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        employe.delete()
        return redirect('employe_list')
    return render(request, 'shop/confirm_delete.html', {'object': employe})

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
@admin_required
def appuser_list(request):
    users = AppUser.objects.all()
    return render(request, 'appuser/appuser_list.html', {'users': users})

def appuser_create(request):
    if request.method == 'POST':
        form = AppUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appuser_list')
    else:
        form = AppUserForm()
    return render(request, 'appuser/appuser_form.html', {'form': form})

@login_required
@admin_required
def appuser_update(request, pk):
    user = get_object_or_404(AppUser, pk=pk)
    if request.method == 'POST':
        form = AppUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('appuser_list')
    else:
        form = AppUserForm(instance=user)
    return render(request, 'appuser/appuser_form.html', {'form': form})

@login_required
@admin_required
def appuser_delete(request, pk):
    user = get_object_or_404(AppUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('appuser_list')
    return render(request, 'appuser/appuser_confirm_delete.html', {'user': user})

# === LOGIN/LOGOUT ===
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Vous êtes connecté en tant que {username}.")
                return redirect('home')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
    form = LoginForm()
    return render(request, 'shop/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('home')

# === ADMIN DASHBOARD ===
@login_required
@admin_required
def admin_dashboard(request):
    # Get counts for each model
    stats = {
        'users': AppUser.objects.count(),
        'employes': Employe.objects.count(),
        'clients': Client.objects.count(),
        'fournisseurs': Fournisseur.objects.count(),
        'categories': Categorie.objects.count(),
        'articles': Article.objects.count(),
        'commandes': Commande.objects.count(),
        'ventes': Vente.objects.count(),
    }
    return render(request, 'shop/admin_dashboard.html', {'stats': stats})

def unauthorized(request):
    return render(request, 'shop/unauthorized.html')
