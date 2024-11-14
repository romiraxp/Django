from django.contrib import admin
from .models import Advertisement, AdvertisementStatusChoices

# Register your models here.
@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    pass

# @admin.register(AdvertisementStatusChoices)
# class AdvertisementStatusChoicesAdmin(admin.ModelAdmin):
#     pass