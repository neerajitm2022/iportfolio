from django.db import models

# Create your models here.
class Crude(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self) -> str:
        return super().__str__()