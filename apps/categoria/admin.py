from django.contrib import admin
from .models import Item
# Configuración del modelo Item
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)  # Añade un filtro lateral

# Registro del modelo Item con su configuración
admin.site.register(Item, ItemAdmin)

# Register your models here.
