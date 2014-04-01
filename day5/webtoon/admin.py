from django.contrib import admin
from webtoon.models import *

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')

admin.site.register(Author, AuthorAdmin)
