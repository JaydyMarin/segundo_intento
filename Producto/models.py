from django.db import models

# Create your models here.
class Producto(models.Model):
  referencias = models.CharField(max_length=200)
  nombre= models.CharField(max_length=200)
  descripcion = models.TextField()
  fechaingreso=models.DateTimeField(auto_now_add=True)