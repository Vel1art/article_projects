from django.contrib import admin

from webapp.models import Article


class TagInline(admin.TabularInline):
    model = Article.tags.through

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',  'created_at']
    list_display_links = ['id', 'title']
    list_filter = []
    search_fields = ['title', 'content']
    fields = ['title',  'content',  'created_at', 'updated_at',]
    readonly_fields = ['created_at', 'updated_at']
    # filter_horizontal = ['tags']
    inlines = [TagInline]