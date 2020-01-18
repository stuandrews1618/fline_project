from django.db import models

class CompanyType(models.Model):
    company_type = models.CharField(verbose_name='Type of Company', max_length=100,)

    def __str__(self):
        return self.company_type