from django.db import models

# Create your models here.
class musician(models.Model):
    first_Name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=12)
    Instrument_Type =models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_Name