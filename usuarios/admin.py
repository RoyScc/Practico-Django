from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {
            'fields': (
                'foto',
                'telefono',
                'preferencia_peliculas',
            )
        }),
    )

    list_display = (
        'username',
        'email',
        'telefono',
        'is_staff',
    )