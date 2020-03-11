from django.db import models


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок статьи', max_length=200)
    text = models.TextField(verbose_name='Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title


class Comment(models.Model):
    question = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('Автор комментирия', max_length=50)
    text = models.CharField(verbose_name='Текст комментирия', max_length=300)
    created_date = models.DateTimeField('Дата создания')

    def __str__(self):
        return self.author
