from django.db import models


# Create your models here.



class modulesdetails(models.Model):
    modulecode = models.CharField(max_length=255, null=True,blank=True)
    modulename = models.CharField(max_length=255, null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    details = models.CharField(max_length=955, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.modulename
    
    
    
    
class postassignments(models.Model):
    modulename = models.CharField(max_length=255, null=True,blank=True)
    modulecode = models.CharField(max_length=255, null=True,blank=True)
    releasedate = models.DateTimeField()
    duedate = models.DateTimeField()
    question = models.CharField(max_length=955, null=True,blank=True)
    file = models.FileField(upload_to="upload/Assignmentque", null=True, blank=True)
    message = models.CharField(max_length=955, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    

    
    def __str__(self):
        return self.question
    
    
    
class studentpostassignment(models.Model):
    studentname = models.CharField(max_length=255, null=True,blank=True)
    modulename = models.CharField(max_length=255, null=True,blank=True)
    file = models.FileField(upload_to="upload/Assignmentque", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.studentname
    
    
    
class teacherfeedback(models.Model):
    To = models.CharField(max_length=255, null=True,blank=True)
    message = models.CharField(max_length=255, null=True,blank=True)
    feedback = models.CharField(max_length=255, null=True,blank=True)
    
    def __str__(self):
        return self.message
    
    
    
class uploadassignments(models.Model):
    file = models.FileField(upload_to="upload/Assignmentsub", null=True, blank=True)
    subject = models.CharField(max_length=255, null=True,blank=True)
    Name = models.CharField(max_length=255, null=True,blank=True)
    message = models.CharField(max_length=255, null=True,blank=True)
    submittedon = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message
    
    
    
    
    
    
class studentmsg(models.Model):
    Name = models.CharField(max_length=255, null=True,blank=True)
    subject = models.CharField(max_length=255, null=True,blank=True)
    message = models.CharField(max_length=255, null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message
    