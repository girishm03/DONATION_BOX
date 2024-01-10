from django.db import models

# Create your models here.

class CategoryDB(models.Model):
    C_name = models.CharField(max_length=100, null=True, blank=True)
    Desciption = models.CharField(max_length=100, null=True, blank=True)
    C_image = models.ImageField(upload_to="CIMAGE", null=True, blank=True)

class WebsiteDB(models.Model):
    WebName = models.CharField(max_length=100, null=True, blank=True)
    WebAbout = models.CharField(max_length=100, null=True, blank=True)
    WebImage = models.ImageField(upload_to="WEBIMAGE", null=True, blank=True)

class PersonDB(models.Model):
    Pname = models.CharField(max_length=100, null=True, blank=True)
    Pemail = models.CharField(max_length=100, null=True, blank=True)
    Pgender = models.CharField(max_length=100, null=True, blank=True)
    Plocation = models.CharField(max_length=100, null=True, blank=True)
    Poccupation = models.CharField(max_length=100, null=True, blank=True)
    Pcategory = models.CharField(max_length=100, null=True, blank=True)
    pDOV = models.CharField(max_length=100, null=True, blank=True)
    pamount = models.IntegerField(null=True, blank=True)
    Pabout = models.CharField(max_length=100, null=True, blank=True)
    Pimage = models.ImageField(upload_to="PIMAGE", null=True, blank=True)

