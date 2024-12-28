from django.db import models

class saveenquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=60)
    phone=models.CharField(max_length=50)
    websiteLink=models.CharField(max_length=70)
    message=models.TextField()
    
    
    

# Create your models here.
