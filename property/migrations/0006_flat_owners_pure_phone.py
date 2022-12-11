# Generated by Django 2.2.24 on 2022-12-02 04:35

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_flat_likes_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owners_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, verbose_name='Нормализованный номер владельца'),
        ),
    ]