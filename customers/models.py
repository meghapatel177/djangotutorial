from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_name = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name

class Software(models.Model):
    customer_pk = models.CharField(max_length=200)
    software_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.software_name
