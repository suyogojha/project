from django.contrib import admin
from databaseproject.models import *

# Register your models here.
@admin.register(modulesdetails)
class modulesdetailsAdmin(admin.ModelAdmin):
    list_display = ("modulecode", "modulename","description","details")



@admin.register(postassignments)
class postassignmentsAdmin(admin.ModelAdmin):
    list_display = ("modulecode", "modulename","releasedate","question")


@admin.register(studentpostassignment)
class studentpostassignmentAdmin(admin.ModelAdmin):
    list_display = ("studentname", "modulename")




@admin.register(teacherfeedback)
class teacherfeedbackAdmin(admin.ModelAdmin):
    list_display = ("To", "message", "feedback")


@admin.register(uploadassignments)
class uploadassignmentsAdmin(admin.ModelAdmin):
    list_display = ("Name", "subject", "file",  "message", "submittedon")

@admin.register(studentmsg)
class studentmsgAdmin(admin.ModelAdmin):
    list_display = ("Name", "subject","message", "time")








