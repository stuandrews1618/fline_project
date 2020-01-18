from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    #title = models.CharField(verbose_name="Title",max_length=250,blank=True)
    def __str__(self):
        return self.email

# Create your models here.
