from django.contrib import admin
from .models import Articulos

from .models import Contactos



# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'producto', 'precio','correo', 'descripcion', 'numero')
    search_fields =('nombre', 'producto', 'precio', 'numero')
    date_hierarchy = 'created'
<<<<<<< Updated upstream
    list_filter =('nombre', 'producto', 'precio', 'numero')
admin.site.register(Articulos, AdministrarModelo)
=======
    list_filter =('id', 'producto', 'precio',)
admin.site.register(Articulos, AdministrarModelo)
admin.site.register(Contactos)





>>>>>>> Stashed changes
