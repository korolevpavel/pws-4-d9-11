# Generated by Django 2.2.7 on 2020-03-07 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20200229_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
