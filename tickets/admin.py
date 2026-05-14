from django.contrib import admin
from .models import Tickets, MetodoPago

@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_filter = ('tipo',) 
    search_fields = ('nombre',)

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_filter = ('nombre',) 
    search_fields = ('nombre',)
