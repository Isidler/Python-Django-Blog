from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /articles/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:article_id>/comment/', views.comment, name='comment')
    # # ex: /articles/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
]
