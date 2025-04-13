from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    telephone = models.CharField(max_length=15)
    cni = models.CharField(max_length=15)
    adresse = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)

class Fournisseur(models.Model):
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    telephone = models.CharField(max_length=45)
    adresse = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Employe(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Categorie(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

class Article(models.Model):
    nom_article = models.CharField(max_length=50)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix_unitaire = models.IntegerField()
    date_expiration = models.DateTimeField()
    date_fabrication = models.DateTimeField()

    def __str__(self):
        return self.nom_article

class Commande(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix = models.IntegerField()
    date_commande = models.DateTimeField()

class Vente(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix = models.IntegerField()
    date_vente = models.DateTimeField()
