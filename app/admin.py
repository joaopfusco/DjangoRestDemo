from django.contrib import admin
from .models import *

class BaseAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_per_page = 10
    list_display = ("id", "created_at", "updated_at",)

class ItemAdmin(BaseAdmin):
    list_display = BaseAdmin.list_display + ("name",) 

admin.site.register(ItemModel, ItemAdmin)