from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'photo', 'created_at', 'updated_at')
    list_display_links = ('name', 'slug')
    # fields = ('name', 'slug', 'photo')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', 'slug',)
