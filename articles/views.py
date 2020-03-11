from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect

from .models import Article, Comment
from django.urls import reverse
from django.utils import timezone


def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'index.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'detail.html', {'article': article})


# def results(request, article_id):
#     question = get_object_or_404(Article, pk=article_id)
#     return render(request, 'results.html', {'article': article})


def comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.comment_set.create(
        author=request.POST['author'], text=request.POST['comment_text'], created_date=timezone.now())
    article.save()
    return render(request, 'detail.html', {'article': article})
