from __future__ import unicode_literals
from foods.models import Foods
from django.db import models
from django.contrib.auth.models import User


class Comments(models.Model):
    food = models.ForeignKey(Foods, on_delete = models.CASCADE, verbose_name = 'Food', blank = True,null = True, related_name = 'comments_food')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Author comment', blank = True,null = True)
    create_date = models.DateTimeField(auto_now = True)
    text = models.TextField(verbose_name = 'Text comment')
    status = models.BooleanField(verbose_name = 'Status comment', default = False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Comments'