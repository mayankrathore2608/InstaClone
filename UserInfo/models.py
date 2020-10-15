from django.db import models


# Create your models here.
class UserCred(models.Model):
    username = models.CharField(max_length=500, primary_key=True,default=None)
    password = models.CharField(max_length=500,blank=False,default=None)
    name = models.CharField(max_length=400,blank=False,default=None)
    email = models.CharField(max_length=500,blank=False)

    def __str__(self):
        return self.username
