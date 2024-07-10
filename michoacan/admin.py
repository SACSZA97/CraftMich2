from django.contrib import admin
from .models import CrearEvento

# Register your models here.
class administrarCrearEvento(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('id','nombre')
    date_hierarchy = 'fecha'
    readonly_fields = ('id', 'fecha')
admin.site.register(CrearEvento, administrarCrearEvento)