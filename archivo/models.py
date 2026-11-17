from django.db import models

# Modelo para las áreas o departamentos del ISSSTE
class Area(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Área")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

# Modelo para los documentos o registros del archivo
class Documento(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del Documento")
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código / Folio")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Área Responsable")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")

    def __str__(self):
        return f"{self.codigo} - {self.titulo}"