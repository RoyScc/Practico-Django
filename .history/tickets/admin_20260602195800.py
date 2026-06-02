from django.contrib import admin
from django.utils.html import format_html
from .models import Tickets, MetodoPago

@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_filter = ('tipo',) 
    search_fields = ('nombre',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="200" />', obj.imagen.url)
        return "No hay imagen disponible"
    preview.short_description = "Vista previa"

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_filter = ('nombre',) 
    search_fields = ('nombre',)
