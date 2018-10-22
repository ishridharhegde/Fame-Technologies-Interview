from django.db import models
import random
import barcode 
from barcode.writer import ImageWriter


class BlogPost(models.Model):
    title = models.CharField(max_length=140) 
    date = models.DateTimeField()
    employeeBarcode = models.ImageField(blank=True, upload_to="users/")
    employeeID = models.IntegerField(default="100")
    
    def __str__(self):
        return self.title

def __init__(self):
    ean = barcode.get('ean13', '123456789102', writer=ImageWriter())
    ean = ean.save('ean13')