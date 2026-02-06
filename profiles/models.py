from django.db import models

# Create your models here.
class profiles(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=40)
    tech = models.CharField(max_length=200)
    email = models.EmailField()
    photo = models.ImageField(upload_to='images/')
    doc = models.FileField(upload_to='documents/')
    class Meta:
        db_table = "ProfilesInfo"