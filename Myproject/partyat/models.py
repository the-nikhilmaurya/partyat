from datetime import datetime, timezone
from django.db import models

# Create your models here.
class Venues(models.Model):
    venue_name = models.CharField(max_length=50)
    tables = models.IntegerField()
    # date = models.DateField(default=datetime.now())

    date = models.DateField(default=29)
    # time = models.TimeField(default=datetime.now())

    time = models.TimeField(default=2)
