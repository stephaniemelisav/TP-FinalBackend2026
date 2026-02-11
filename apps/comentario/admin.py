from django.contrib import admin
from apps.comentario.models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("ticket", "usuario", "activo", "fecha_creacion", "fecha_actualizacion")
    list_filter = ("activo", "fecha_creacion", "fecha_actualizacion")
    search_fields = ("contenido", "usuario__username", "ticket__titulo")
