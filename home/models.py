from django.db import models

# Create your models here.
class NavbarItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class AboutUs(models.Model):
    # Definición de campos para el modelo AboutUs
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    

class Service(models.Model):
    # Campos para el modelo de Servicios
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title