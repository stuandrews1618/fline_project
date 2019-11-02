from django.db import models
from django.conf import settings
# from common.models import User


class Company(models.Model):
    company_name = models.CharField('Company Name',max_length=255,blank=False,null=False,unique=True)
    website = models.URLField('Website',max_length=255,blank=True)
    # assigned_to = models.ForeignKey()


