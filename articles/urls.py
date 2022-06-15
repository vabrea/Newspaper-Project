from django.urls import path
from .views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleUpdateView
from articles import views

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('headlines/', views.HeadlineArticleListView.as_view(), name='headline_list'),
    path('sports/', views.SportsArticleListView.as_view(), name='sports_list'),
    path('spiderman/', views.SpidermanArticleListView.as_view(), name='spider_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    ]