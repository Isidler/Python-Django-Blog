import datetime

from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок статьи', max_length=200)
    text = models.TextField(verbose_name='Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def get_last_comments(self):
        return self.comment_set.order_by('-created_date')[:10]


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('Автор комментирия', max_length=50)
    text = models.CharField(verbose_name='Текст комментирия', max_length=300)
    created_date = models.DateTimeField('Дата создания')

    def __str__(self):
        return self.author
