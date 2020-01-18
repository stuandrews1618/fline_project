from django.db import models

class Contact(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    qfl_relationship = models.TextField(max_length = 100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name   
