from django.contrib.contenttypes.models import ContentType
from django.db import models
from webapp.models import BaseModel
from django.apps import apps

class Comment(BaseModel):
    text = models.TextField(verbose_name='Текст комментария')
    article = models.ForeignKey('webapp.Article', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, verbose_name='Автор')

    def like_count(self):
        Like = apps.get_model('webapp', 'Like')
        content_type = ContentType.objects.get_for_model(self)
        return Like.objects.filter(content_type=content_type, object_id=self.pk).count()

    def __str__(self):
        return f'Комментарий {self.id} к статье {self.article}'
