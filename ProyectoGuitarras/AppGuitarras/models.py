from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Fender(models.Model):

    def __str__(self):

        return f"Guitarra Fender: {self.fenderguitarra} ------- Serie: {self.serie}"

    fenderguitarra = models.CharField(max_length=60)
    serie = models.IntegerField()

    
class Gibson(models.Model):

    def __str__(self):

        return f"Guitarra Gibson: {self.gibsonguitarra} ------- Serie: {self.serie}"

    gibsonguitarra = models.CharField(max_length=60)
    serie = models.IntegerField()

class Ibanez(models.Model):

    def __str__(self):

        return f"Guitarra Ibanez: {self.ibanezguitarra} ------- Serie: {self.serie}"

    ibanezguitarra = models.CharField(max_length=60)
    serie = models.IntegerField()


class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
