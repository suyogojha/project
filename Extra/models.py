from pyexpat import model
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField




# Create your models here.
class mycertificatespic(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    image = models.ImageField(upload_to="upload/certificates", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
class projectcodes(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    new_slug = AutoSlugField(populate_from='name',unique=True,null=True,default=None)
   
    
    def __str__(self):
        return self.name
    
    


class videosmyproject(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    url = models.CharField(max_length=255, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.name
    
    
    
class myteamimg(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    position = models.CharField(max_length=255, null=True,blank=True)
    image = models.ImageField(upload_to="upload/MyTeam", null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True,blank=True)
    insta_url = models.CharField(max_length=255, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name