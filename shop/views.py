from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Commande, Vente, Fournisseur, Client, Categorie, Employe
from .forms import ArticleForm, CommandeForm, VenteForm, FournisseurForm, ClientForm, CategorieForm, EmployeForm

# === ARTICLE ===
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'shop/article_list.html', {'articles': articles})

def article_create(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'shop/form.html', {'form': form})

def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'shop/form.html', {'form': form})

def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'shop/confirm_delete.html', {'object': article})


# === COMMANDE ===
def commande_list(request):
    commandes = Commande.objects.all()
    return render(request, 'shop/commande_list.html', {'commandes': commandes})

def commande_create(request):
    form = CommandeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('commande_list')
    return render(request, 'shop/form.html', {'form': form})

def commande_update(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    form = CommandeForm(request.POST or None, instance=commande)
    if form.is_valid():
        form.save()
        return redirect('commande_list')
    return render(request, 'shop/form.html', {'form': form})

def commande_delete(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('commande_list')
    return render(request, 'shop/confirm_delete.html', {'object': commande})


# === VENTE ===
def vente_list(request):
    ventes = Vente.objects.all()
    return render(request, 'shop/vente_list.html', {'ventes': ventes})

def vente_create(request):
    form = VenteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('vente_list')
    return render(request, 'shop/form.html', {'form': form})

def vente_update(request, pk):
    vente = get_object_or_404(Vente, pk=pk)
    form = VenteForm(request.POST or None, instance=vente)
    if form.is_valid():
        form.save()
        return redirect('vente_list')
    return render(request, 'shop/form.html', {'form': form})

def vente_delete(request, pk):
    vente = get_object_or_404(Vente, pk=pk)
    if request.method == 'POST':
        vente.delete()
        return redirect('vente_list')
    return render(request, 'shop/confirm_delete.html', {'object': vente})


# === FOURNISSEUR ===
def fournisseur_list(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'shop/fournisseur_list.html', {'fournisseurs': fournisseurs})

def fournisseur_create(request):
    form = FournisseurForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fournisseur_list')
    return render(request, 'shop/form.html', {'form': form})

def fournisseur_update(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    form = FournisseurForm(request.POST or None, instance=fournisseur)
    if form.is_valid():
        form.save()
        return redirect('fournisseur_list')
    return render(request, 'shop/form.html', {'form': form})

def fournisseur_delete(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('fournisseur_list')
    return render(request, 'shop/confirm_delete.html', {'object': fournisseur})


# === CLIENT ===
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'shop/client_list.html', {'clients': clients})

def client_create(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'shop/form.html', {'form': form})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'shop/form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'shop/confirm_delete.html', {'object': client})


# === CATEGORIE ===
def categorie_list(request):
    categories = Categorie.objects.all()
    return render(request, 'shop/categorie_list.html', {'categories': categories})

def categorie_create(request):
    form = CategorieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('categorie_list')
    return render(request, 'shop/form.html', {'form': form})

def categorie_update(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    form = CategorieForm(request.POST or None, instance=categorie)
    if form.is_valid():
        form.save()
        return redirect('categorie_list')
    return render(request, 'shop/form.html', {'form': form})

def categorie_delete(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('categorie_list')
    return render(request, 'shop/confirm_delete.html', {'object': categorie})


# === EMPLOYE ===
def employe_list(request):
    employes = Employe.objects.all()
    return render(request, 'shop/employe_list.html', {'employes': employes})

def employe_create(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('employe_list')
    return render(request, 'shop/form.html', {'form': form})

def employe_update(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    form = EmployeForm(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        return redirect('employe_list')
    return render(request, 'shop/form.html', {'form': form})

def employe_delete(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        employe.delete()
        return redirect('employe_list')
    return render(request, 'shop/confirm_delete.html', {'object': employe})

def home(request):
    return render(request, 'home.html')