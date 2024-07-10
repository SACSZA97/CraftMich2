from django.db import models

# Create your models here.
class Articulos(models.Model):

    Art = [
        ('Jarras', 'Jarras'),
        ('Vasos', 'Vasos'),
        ('Platos', 'Platos'),
        ('Catrinas', 'Catrinas'),
        ('Bolsos', 'Bolsos'),
        ('Suter', 'Suter'),
    ]
    
    nombre = models.TextField() #Texto largo
    producto = models.CharField(max_length=20, choices=Art, default='Artesania', verbose_name="Producto")
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    precio = models.PositiveIntegerField(default=0)
    correo = models.EmailField (max_length=254, default='example@example.com')
    descripcion = models.TextField(default='Descripcion') #Texto largo
    numero = models.CharField(max_length=15)
    facebook = models.URLField(max_length=255)
    instagram = models.URLField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado") #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-created"]
        #el menos indica que se ordenara del más reciente al más viejo
    
    def __str__(self):

        return self.nombre
        #Indica que se mostrára el nombre como valor en la tabla