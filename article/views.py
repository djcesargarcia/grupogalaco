from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required
def articles(request):
    if 'qtext' in request.GET:
        qtext = request.GET['qtext']
        articles = Article.objects.filter(name__icontains=qtext)
    else: 
        articles = Article.objects.all()
        page = request.GET.get('page',1)
        paginator = Paginator(articles, 5)
        try:
            articles = paginator.page(page)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
    return render(request, 'articles/index.html', {'articles':articles})

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