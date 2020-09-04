from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from main import models

# Create your views here.
def index(request):
    latest_article = models.Article.objects.all().order_by('-createdAt')[:10]
    context = {
        'latest_article': latest_article
    }
    return render(request, 'main/index.html', context)
    
def article(request,pk):
    article= get_object_or_404(models.Article,pk=pk)
    context = {
        'article':article
    }
    return render(request, 'main/article.html', context)

def article1(request):
    article= get_object_or_404(models.Article)
    context = {
        'article':article
    }
    return render(request, 'main/article.html', context)

def author(request, pk):
    author = get_object_or_404(models.Author,pk=pk)
    context = {
        'author': author
    }
    return render(request, 'main/author.html', context)

def create(request):
    authors = models.Author.objects.all()
    context = {
        'authors': authors
    }
    if request.method == "POST":
        article_data = {
            "title": request.POST['title'],
            "content": request.POST['content'],
            "file":request.POST['file']
        }
        article = models.Article.objects.create(**article_data)
        author = models.Author.objects.filter(pk=request.POST['author'])
        article.authors.set(author)
        context["sucess"] = True
    return render(request,'main/create.html',context)