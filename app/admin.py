from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'status', 'updated',
                    'publication_date')


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    pass
