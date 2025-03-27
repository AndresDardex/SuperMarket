from django.contrib import admin
from .models import Cliente, PQRS

class PQRSInline(admin.TabularInline):  # O usa admin.StackedInline para un diseño diferente
    model = PQRS
    extra = 1  # Número de formularios vacíos adicionales para agregar nuevos registros

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_identificacion', 'numero_identificacion', 'nombre_completo', 'correo_electronico', 'telefono_movil', 'tipo', 'validacion')
    list_filter = ('tipo', 'validacion', 'tipo_identificacion')  # Filtros laterales
    search_fields = ('nombre_completo', 'numero_identificacion', 'correo_electronico')  # Barra de búsqueda
    inlines = [PQRSInline]  # Agrega la edición en línea de PQRS

@admin.register(PQRS)
class PQRSAdmin(admin.ModelAdmin):
    list_display = ('numero_radicado', 'fecha_radicado', 'tipo_radicado', 'comentarios', 'anexo', 'cliente')
    list_filter = ('tipo_radicado', 'fecha_radicado')  # Filtros laterales
    search_fields = ('numero_radicado', 'cliente__nombre_completo')  # Barra de búsqueda