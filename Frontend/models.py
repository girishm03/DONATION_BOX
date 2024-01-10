from django.db import models

# Create your models here.

class RegisterDB(models.Model):
    UserName = models.CharField(max_length=100, null=True, blank=True)
    Mobile_Number = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
class contributionDB(models.Model):
    CName = models.CharField(max_length=100, null=True, blank=True)
    CMobile = models.IntegerField(null=True, blank=True)
    Cemail = models.CharField(max_length=100, null=True, blank=True)
    Cmessage = models.CharField(max_length=100, null=True, blank=True)
    Ccategory = models.CharField(max_length=100, null=True, blank=True)
    Coccupation = models.CharField(max_length=100, null=True, blank=True)
    Camount = models.IntegerField(null=True, blank=True)
    Cfile = models.FileField(upload_to="DFILE", null=True, blank=True)

class itemsDB(models.Model):
    IName = models.CharField(max_length=100, null=True, blank=True)
    IMobile = models.IntegerField(null=True, blank=True)
    Iemail = models.CharField(max_length=100, null=True, blank=True)
    Ilocation = models.CharField(max_length=100, null=True, blank=True)
    Iitem = models.CharField(max_length=100, null=True, blank=True)
