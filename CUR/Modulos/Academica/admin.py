from django.contrib import admin
from Modulos.Academica.models import *


# Register your models here.
class carreraAdmin(admin.ModelAdmin):
    list_display = ("snies", "nombre", "duracion", "modalidad")
    search_fields = ("snies", "nombre", "modalidad")
    list_filter = ("modalidad", "duracion")
    ordering = ("nombre", "duracion")


admin.site.register(Carrera, carreraAdmin)


class estudianteAdmin(admin.ModelAdmin):
    list_display = (
        "numDocumento",
        "nombres",
        "apellidoPaterno",
        "apellidoMaterno",
        "carrera",
    )
    search_fields = ("numDocumento", "nombres", "apellidoPaterno", "apellidoMaterno")
    ordering = ("nombres", "apellidoPaterno", "apellidoMaterno", "carrera")


admin.site.register(Estudiante, estudianteAdmin)


class docenteAdmin(admin.ModelAdmin):
    list_display = ("numDocumento", "nombres", "apellidoPaterno", "apellidoMaterno")
    search_fields = ("numDocumento", "nombres", "apellidoPaterno", "apellidoMaterno")
    ordering = ("nombres", "apellidoPaterno", "apellidoMaterno")


admin.site.register(Docente, docenteAdmin)


class semestreAdmin(admin.ModelAdmin):
    list_display = ("descripción", "totalCreditos")
    search_fields = ("descripción", "totalCreditos")
    ordering = ("descripción", "totalCreditos")


admin.site.register(Semestre, semestreAdmin)


class cursoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "docente")
    search_fields = ("codigo", "nombre", "docente")
    ordering = ("codigo", "nombre", "docente")


admin.site.register(Curso, cursoAdmin)

admin.site.register(Matricula)


admin.site.register(Programa)


class facultadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion")
    search_fields = ("nombre", "direccion")
    ordering = ("nombre", "direccion")


admin.site.register(Facultad, facultadAdmin)
