from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, FormView, ListView
from webapp.forms import ArticleForm
from webapp.models import Article


class ArticleListView(ListView):
    model = Article
    # queryset = Article.objects.filter(title__icontains='article')
    template_name = 'articles/index.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

    # def get_queryset(self):
    #     return super().get_queryset().filter(title__icontains='article')


class ArticleDetailView(TemplateView):
    template_name = 'articles/article_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        return context


class ArticleCreateView(FormView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm

    # def get_success_url(self):
    #     return reverse('article_detail', kwargs={'pk': self.article.pk})

    def form_valid(self, form):
        article = form.save()
        return redirect('article_detail', pk=article.pk)

class ArticleUpdateView(FormView):
    template_name = 'articles/article_update.html'
    form_class = ArticleForm

    def dispatch(self, request, *args, **kwargs):
        self.article = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.article
        return context

    def get_object(self):
        return get_object_or_404(Article, pk=self.kwargs.get('pk'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

    def form_valid(self, form):
        self.article = form.save()
        return redirect('article_detail', pk=self.article.id)

class ArticleDeleteView(View):
    def dispatch(self, request, *args, **kwargs):
        self.article = get_object_or_404(Article, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'articles/article_delete.html', context={'article': self.article})

    def post(self, request, *args, **kwargs):
        self.article.delete()
        return redirect('articles')
