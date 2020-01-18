from django.db import models
from django.conf import settings
from users.models import CustomUser
from common.models import CompanyType


class Company(models.Model):
    company_name = models.CharField(verbose_name='Company Name',max_length=255,blank=False,null=False,unique=True)
    website = models.URLField(verbose_name='Website',max_length=255,blank=True)
    assigned_to = models.ForeignKey('users.CustomUser',on_delete=models.DO_NOTHING)
    company_type = models.ForeignKey('common.CompanyType', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.company_name


