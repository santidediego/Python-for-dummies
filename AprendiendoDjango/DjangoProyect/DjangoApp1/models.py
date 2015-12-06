from django.db import models
from django.template.defaultfilters import slugify

class Bares(models.Model):
    nombre = models.CharField(max_length=30, unique=True, null=False)
    direccion = models.CharField(max_length=50, unique=True, null=False)
    num_visitas=models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Bares, self).save(*args, **kwargs)

    #That´s for use print after. When we use print(Bares) it will show only the name
    def __str__(self):  #For Python 2, use __str__ on Python 3
        return self.nombre

class Tapas(models.Model):
    bar=models.ForeignKey(Bares, null=False) #We define the foreign key
    nombre = models.CharField(max_length=30, unique=True, null=False)
    votos=models.IntegerField(default=0)

    def __str__(self):      #For Python 2, use __str__ on Python 3
        return self.nombre
