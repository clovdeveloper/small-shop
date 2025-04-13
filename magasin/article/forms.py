# forms.py
from django import forms

from magasin.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'date_expiration': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_fabrication': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
