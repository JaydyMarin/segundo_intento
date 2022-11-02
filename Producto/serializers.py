from dataclasses import fields
from rest_framework import serializers

from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
  class Meta:
    model=Producto
    fields=('id','referencias','nombre','descripcion','fechaingreso')
    read_only_fields = ('fechaingreso',)