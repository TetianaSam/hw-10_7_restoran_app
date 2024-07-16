
from django.db import models

# Create your models here.
class List(models.Model):
  resto_name = models.CharField(max_length=255)
  resto_specialization = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  website = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=255)

  def __str__(self):
      return (f"{self.resto_name} "
              f"{self.resto_specialization} "
              f"{self.address} "
              f"{self.website}"
              f"{self.phone_number}"
              )
