from django.db import models

class Productos(models.Model):
    idProd = models.AutoField(primary_key = True)
    nombreProd = models.CharField(max_length = 50, blank = False, null = False)
    fabricante = models.CharField(max_length = 50, blank = False, null = False)
    descripcion = models.CharField(max_length = 300, blank = False, null = False)
    imagen =models.ImageField(upload_to=None, null = True)

    class Meta:
        verbose_name = ("Producto")
        verbose_name_plural = ("Productos")

    def __str__(self):
        return self.nombreProd


