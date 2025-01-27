from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from webapp.models import Comment, Like
from django.contrib.contenttypes.models import ContentType

@login_required
def toggle_like_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    user = request.user
    content_type = ContentType.objects.get_for_model(Comment)

    like, created = Like.objects.get_or_create(content_type=content_type, object_id=comment.pk, user=user)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({'liked': liked, 'like_count': comment.like_count()})
