from webtoon.models import *
from django.contrib import admin
 
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
admin.site.register(Author, AuthorAdmin)
 
class ComicAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'desc')
admin.site.register(Comic, ComicAdmin)
 
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('comic', 'title', 'pub_date')
admin.site.register(Episode, EpisodeAdmin)
 
class CommentAdmin(admin.ModelAdmin):
    list_display = ('episode', 'user', 'msg', 'written_date')

admin.site.register(Comment, CommentAdmin)
