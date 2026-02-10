from django.db import models
from django.contrib.auth.models import AbstractUser

# Se hereda abstractuser por si en un futuro se requiere ampliar los atributos de un usuario.
class Usuario(AbstractUser):
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def __str__(self):
        return self.username