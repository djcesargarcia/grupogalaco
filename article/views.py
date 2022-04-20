from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html',{'articles': articles})

@login_required
def create_articles(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('articles')
    return render(request, 'articles/create.html',{'form':form})

@login_required
def edit_articles(request, id):
    article = Article.objects.get(id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid and request.POST:
        form.save()
        return redirect('articles')
    return render(request,'articles/edit.html',{'form':form})

@login_required
def delete_articles(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles')