from django.db import models

# Create your models here.
class Contact(models.Model):
    title = models.CharField(max_length=200, verbose_name='titulo')
    content = models.TextField(verbose_name="contenido")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de modificación")
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "contacto"
        verbose_name_plural = "contactos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
