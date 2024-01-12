from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class formdetails(models.Model):
    Name=models.CharField(max_length=250)
    DOB = models.CharField(max_length=250)
    Age = models.CharField(max_length=250)
    Gender = models.CharField(max_length=250)
    Phone = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    Address = models.TextField(max_length=250)
    District= models.CharField(max_length=250)
    Branch = models.CharField(max_length=250)
    Account_Type = models.CharField(max_length=250)
    Materials_Provided = models.CharField(max_length=250)
    class Meta:
        db_table='formdetails'
    def _str_(self):
        return self.Name





