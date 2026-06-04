from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

class UsuarioPersonalizadoAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información Extra', {'fields': ('telefono', 'foto', 'preferencia_peliculas')}),
    )


admin.site.register(UsuarioPersonalizado, UsuarioPersonalizadoAdmin)