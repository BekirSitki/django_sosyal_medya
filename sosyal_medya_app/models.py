from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    yazar = models.ForeignKey( User, on_delete=models.CASCADE )
    icerik = models.TextField( )
    paylasma_tarihi = models.DateField( auto_now_add=True )
   