from articles.models import *
from django.contrib import admin

#class ArticleInline(admin.TabularInline):
#    model = Article
#    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'pub_date', 'likes', 'was_published_recently')
    list_filter = ['pub_date']

    search_fields = ['title']

    fieldsets = [
        (None, {'fields': ['title', 'body']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]

    #inlines = [ArticleInline]

admin.site.register(Article, ArticleAdmin)

# Register your models here.
