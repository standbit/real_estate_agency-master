# Generated by Django 2.2.28 on 2022-12-02 07:14
import phonenumbers

from django.db import migrations


def normalize_phones(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phone_obj = phonenumbers.parse(flat.owners_phonenumber, "RU")
        phone_national_number = phone_obj.national_number
        if not phonenumbers.is_valid_number(phone_obj):
            # flat.owners_pure_phone = ''
            # flat.save()
            continue
        if len(str(phone_national_number)) < 10:
            flat.owners_pure_phone = f"+710{phone_obj.country_code}{phone_national_number}"
        else:
            flat.owners_pure_phone = f"+7{phone_national_number}"
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_owners_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phones),
    ]
