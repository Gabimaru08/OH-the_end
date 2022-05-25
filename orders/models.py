from django.db import models
from sqlalchemy import false
from django.contrib.auth.models import User

# Create your models here.
class Platillos(models.Model): 
    nombre = models.CharField(max_length=65, blank=false)
    def __str__(self):
        return self.nombre
