from django.contrib import admin

from .models import Flat
from .models import Complaint
from .models import Owner

@admin.register(Flat)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'owners_phonenumber',
        'owners_pure_phone',)
    list_editable = ('new_building',)
    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony')
    raw_id_fields = ('likes_num',)

@admin.register(Complaint)
class AuthorAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')

@admin.register(Owner)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'owner_name',)
    search_fields = ['owner_name']
    raw_id_fields = ('flats',)