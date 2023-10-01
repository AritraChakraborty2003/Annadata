from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.TextField()
    email=models.TextField()
    designation=models.TextField()
    message=models.TextField()
   
      
   