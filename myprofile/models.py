from django.db import models
from datetime import datetime
# Create your models here.


class About(models.Model):
    description = models.CharField(max_length = 255, null = True)
    birthday = models.DateField(default = datetime.now())
    website = models.CharField(max_length = 255, null = True)
    phone =models.CharField(max_length=200)

    def __str__(self):
        
        return self.description
     
