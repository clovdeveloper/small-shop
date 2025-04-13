# views.py
from django.shortcuts import render, redirect, get_object_or_404

from magasin.article.forms import ArticleForm
from magasin.models import Article


# Create
def article_create(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'article_form.html', {'form': form})

# Read - list
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

# Update
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'article_form.html', {'form': form})

# Delete
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'article_confirm_delete.html', {'article': article})
