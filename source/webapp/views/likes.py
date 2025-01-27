from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from webapp.models import Article, Like

@login_required
def toggle_like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    user = request.user

    like, created = Like.objects.get_or_create(
        content_type=ContentType.objects.get_for_model(Article),
        object_id=article.id,
        user=user
    )

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({'liked': liked, 'like_count': article.like_count()})
