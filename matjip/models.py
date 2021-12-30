from django.db import models
from datetime import datetime

class Place(models.Model):
    name = models.CharField(max_length=200, null=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=False)
    description = models.TextField(null=True)
    created_date = models.DateTimeField(default=datetime.now())
    updated_date = models.DateTimeField(default=datetime.now())
    num_visit = models.IntegerField(default=0)

    def __str__(self):
        return self.name
