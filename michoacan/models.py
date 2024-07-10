from django.db import models


# Create your models here.
class CrearEvento(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Id Evento")
    nombre = models.TextField(verbose_name="Nombre del Evento")
    fecha = models.DateField(verbose_name="Fecha del Evento")
    hora = models.TimeField(verbose_name="Hora del Evento")
    lugar = models.TextField(verbose_name="Lugar del Evento")
    tipo = models.TextField(verbose_name="Tipo de Evento")
    descripcion = models.TextField(verbose_name="Descripcion del Evento")
    class Meta:
        verbose_name = "Crear Evento"
        verbose_name_plural = "Crear Eventos"
        ordering = ["fecha"]
    def __str__(self):
        return self.nombre
