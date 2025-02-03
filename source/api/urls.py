from django.urls import path
from .views import (
    ArticleDetailView, ArticleUpdateView, ArticleDeleteView,
    ArticleCommentsView, CommentDetailView, CommentCreateView,
    CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),

    path('article/<int:pk>/comments/', ArticleCommentsView.as_view(), name='article_comments'),
    path('article/<int:pk>/comment/add/', CommentCreateView.as_view(), name='comment_add'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
