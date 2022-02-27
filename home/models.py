from enum import unique
from django.db import models
from django.db.models.base import Model
from django.utils.safestring import mark_safe
from autoslug import AutoSlugField
# Create your models here.
class contactus(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField(max_length=255, null=True,blank=True)
    subject = models.CharField(max_length=255, null=True,blank=True)
    message = models.TextField(max_length=255, null=True,blank=True)

    def __str__(self):
        return self.name
    
    
class myblog(models.Model):
    title = models.CharField(max_length=255, null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    tags = models.CharField(max_length=255, null=True,blank=True)   
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="upload/image", null=True, blank=True)
    new_slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)

        
    
    
    def __str__(self):
        return self.title
    

class myportfilio(models.Model):
    project = models.CharField(max_length=255, null=True,blank=True)
    donefor = models.CharField(max_length=255, null=True,blank=True)
    langauges = models.CharField(max_length=255, null=True,blank=True)
    preview = models.CharField(max_length=255, null=True,blank=True)
    image = models.ImageField(upload_to="upload/image", null=True, blank=True)

    def __str__(self):
        return self.project
    
    
    
    def myportfolioimage(self):
        return mark_safe('<img src="{}" width="100 />'.format(self.image.url))
    myportfolioimage.short_description = 'image'
    myportfolioimage.allow_tags = True
    
    def __str__(self):
        return self.project
    
        
        
class myskillsabout(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    percentage = models.CharField(max_length=255, null=True,blank=True)
    
    
    def __str__(self):
        return self.name
    
    
class myprofilepic(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    image = models.ImageField(upload_to="upload/profile", null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
    
    
class APILINKANDNAME(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    link = models.CharField(max_length=255, null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    
    
