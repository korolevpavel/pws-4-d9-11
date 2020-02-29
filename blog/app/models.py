from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete = models.CASCADE, null = True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'
