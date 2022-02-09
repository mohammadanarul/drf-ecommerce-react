from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    title = models.CharField(_('title'))

    def __str__(self):
        return 

    def __unicode__(self):
        return 
