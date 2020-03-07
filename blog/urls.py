from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('app.urls', 'posts'))),
    path('admin/', admin.site.urls),
]
