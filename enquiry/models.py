from datetime import datetime
from django.db import models
from contact.models import Contact

qfl_offset = 30000

class Enquiry(models.Model):
    def qfl_no(self):
        self.id + qfl_offset
    qfl_name = models.TextField('QFL Name',max_length=200)
    qfl_address_1 = models.TextField(max_length=100, blank=True)
    qfl_address_2 = models.TextField(max_length=100, blank=True)
    qfl_town = models.TextField(max_length=50, blank=True)
    qfl_postcode = models.TextField(max_length=10)
    qfl_startdate = models.DateTimeField(default=datetime.now)
    qfl_first_contact = models.ForeignKey('contact.Contact',on_delete=models.DO_NOTHING)
    current_total = models.DecimalField('Total Price', max_digits= 10, decimal_places=2)
    def __str__(self):
        return 'QFL{} - {}'.format(self.qfl_no, self.qfl_name)

    @property
    def full_qfl_no(self):
        return 'QFL' + str(self.id + qfl_offset)