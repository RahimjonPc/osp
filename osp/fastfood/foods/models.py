from __future__ import unicode_literals
from django.db import models
import re
from django.contrib.auth.models import User


class Foods(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Owner', blank = True,null = True)
    name = models.CharField(max_length = 50)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters')
    price = models.IntegerField()    
    def __str__(self):
        return self.name    
        
        class Meta:
            verbose_name_plural = 'Foods'
