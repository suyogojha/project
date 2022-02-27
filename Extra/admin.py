from django.contrib import admin
from Extra.models import *
# Register your models here.
@admin.register(mycertificatespic)
class mycertificatespicAdmin(admin.ModelAdmin):
    list_display = ("name","image", "created", "modified")

@admin.register(projectcodes)
class projectcodesAdmin(admin.ModelAdmin):
    list_display = ("name","created", "modified")


@admin.register(videosmyproject)
class videosmyprojectAdmin(admin.ModelAdmin):
    list_display = ("name", "url" ,"created", "modified")


@admin.register(myteamimg)
class myteamimgAdmin(admin.ModelAdmin):
    list_display = ("name", "position","fb_url","insta_url","created", "modified")
