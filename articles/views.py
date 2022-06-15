from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Article
from django.urls import reverse_lazy

class ArticleListView(LoginRequiredMixin,ListView):
    template_name = "articles/list.html"
    model = Article

class HeadlineArticleListView(ArticleListView, LoginRequiredMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_list']= Article.objects.filter(
        section=1).order_by('created_on').reverse()
        context["section"] = "Headlines"
        return context

class SpidermanArticleListView(ArticleListView, LoginRequiredMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_list']= Article.objects.filter(
        section=2).order_by('created_on').reverse()
        context["section"] = "Spider-Man"
        return context

class SportsArticleListView(ArticleListView, LoginRequiredMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_list']= Article.objects.filter(
        section=3).order_by('created_on').reverse()
        context["section"] = "Sports"
        return context

class ArticleCreateView(CreateView,UserPassesTestMixin, LoginRequiredMixin):
    template_name = "articles/new.html"
    model = Article
    fields = ["title", "author", "section","body"]

    def test_func(self):
        return self.request.user.role > 1

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(UpdateView, UserPassesTestMixin,LoginRequiredMixin):
    template_name = "articles/edit.html"
    model = Article
    fields = ["title", "author", "section","body"]

    def test_func(self):
        if self.request.user.role.id > 1:
            article = self.get_object()
            return article.user == self.request.user.role.id > 1
        return False

class ArticleDeleteView(DeleteView, LoginRequiredMixin):
    template_name = "articles/delete.html"
    model = Article
    success_url = reverse_lazy("article_list")
    
    def test_func(self):
        if self.request.user.role.id > 1:
            article = self.get_object()
            return article.user == self.request.user
        return False

class ArticleDetailView(DetailView, LoginRequiredMixin):
    template_name = "articles/detail.html"
    model = Article