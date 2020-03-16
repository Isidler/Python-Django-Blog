from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Article, Comment


class IndexView(generic.ListView):
    template_name = 'articles/index.html'
    context_object_name = 'latest_article_list'
    queryset = Article.objects.filter(
        pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    paginate_by = 2

    # def get_queryset(self):
    #     """Return the last five published articles."""
    #     return Article.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Article
    template_name = 'articles/detail.html'


# def detail(request, article_id):
#     article = get_object_or_404(Article, pk=article_id)
#     return render(request, 'detail.html', {'article': article})


# def results(request, article_id):
#     question = get_object_or_404(Article, pk=article_id)
#     return render(request, 'results.html', {'article': article})


def comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.comment_set.create(
        author=request.POST['author'], text=request.POST['comment_text'], created_date=timezone.now())
    article.save()
    return HttpResponseRedirect(reverse('detail', args=(article.id,)))
