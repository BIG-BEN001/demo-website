from django.db import models
from django.forms import EmailField

# Create your models here.
class EmailMessage(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=128)
    body = models.TextField(max_length=500)