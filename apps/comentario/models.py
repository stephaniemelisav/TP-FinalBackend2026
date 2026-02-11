from django.db import models
from django.conf import settings

class Comentario(models.Model):
    ticket = models.ForeignKey('ticket.Ticket', on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='comentarios_realizados') # esto.. dudo si sea ideal dejarlo en null cuando un usuario sea borrado.
    contenido = models.TextField()

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f"Comentario de {self.usuario} en {self.ticket}"
