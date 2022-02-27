from django.contrib import admin
from home.models import  *

# Register your models here.
@admin.register(contactus)
class contactusAdmin(admin.ModelAdmin):
    list_display = ("name","email", "subject", "message")



@admin.register(myblog)
class myblogAdmin(admin.ModelAdmin):
    list_display = ("title","content", "created", "tags", "modified", "image")


@admin.register(myportfilio)
class myportfilioAdmin(admin.ModelAdmin):
    list_display = ("project","donefor", "langauges", "preview","myportfolioimage","image")
    readonly_fields = ("myportfolioimage",)

@admin.register(myskillsabout)
class myskillsaboutAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage")


@admin.register(myprofilepic)
class myprofilepicAdmin(admin.ModelAdmin):
    list_display = ("name", "image")


@admin.register(APILINKANDNAME)
class APILINKANDNAMEAdmin(admin.ModelAdmin):
    list_display = ("name", "link")



