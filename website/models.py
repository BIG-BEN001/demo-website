from email.policy import default
from random import choices
from tabnanny import verbose
import uuid
from django.conf import settings 
from django.db import models
from django.forms import EmailField
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class EmailMessage(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=128)
    body = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name
    
class BlogCategory(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    title = models.CharField(max_length=100, verbose_name='Title')

    class meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
        ordering=['-title']
        
    def __str__(self):
        return self.title
    
    
class BlogPost(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    
    title = models.CharField(max_length=100)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    header_image = models.ImageField(null=True, blank=False, upload_to='images')
    
    body = RichTextField(blank=False, null=True)
    
    published = models.DateTimeField(default=timezone.now)
    
    created = models.DateTimeField(auto_now_add = True)
    
    published = models.DateTimeField(auto_now = True)
    
    category = models.ForeignKey('BlogCategory', verbose_name='Category', on_delete=models.CASCADE)
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')
    
    class meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_article", args=[self.id])
    