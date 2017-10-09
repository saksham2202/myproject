from django.db import models
from django.utils import timezone
# Create your models here.
class complain(models.Model):

 complaint_date=models.DateTimeField(default=timezone.now)
 location=models.CharField(max_length=50)
 specific_location=models.CharField(max_length=50)
 details=models.CharField(max_length=100)

 class Meta:
  db_table= "complaint"
