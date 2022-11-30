# Generated by Django 2.2.24 on 2022-11-30 07:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20221130_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='likes_num',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_ads', to=settings.AUTH_USER_MODEL, verbose_name='Кто-то лайкнул:'),
        ),
    ]