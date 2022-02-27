from dataclasses import fields
from rest_framework import serializers
from .models import myskillsabout, contactus, myblog, myportfilio
from Extra.models import *


class skillsserializers(serializers.ModelSerializer):
    class Meta:
        model = myskillsabout
        fields = '__all__'
        
        
        
class contactusserializers(serializers.ModelSerializer):
    class Meta:
        model = contactus
        fields = '__all__'
        
        
        
class myblogserializers(serializers.ModelSerializer):
    class Meta:
        model = myblog
        fields = '__all__'
              
class myportfilioserializers(serializers.ModelSerializer):
    class Meta:
        model = myportfilio
        fields = '__all__'
              
        
               
class mycertificatespicserializers(serializers.ModelSerializer):
    class Meta:
        model = mycertificatespic
        fields = '__all__'
              

class projectcodesserializers(serializers.ModelSerializer):
    class Meta:
        model = projectcodes
        fields = '__all__'
              
class videosmyprojectserializers(serializers.ModelSerializer):
    class Meta:
        model = videosmyproject
        fields = '__all__'
              
class myteamimgserializers(serializers.ModelSerializer):
    class Meta:
        model = myteamimg
        fields = '__all__'
              
                                
        
                      
        
        
        
