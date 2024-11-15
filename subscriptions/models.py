
from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50,null=True)
    number = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
