from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.usuario.models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_superuser", "is_active",)
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "email", "first_name", "last_name")
