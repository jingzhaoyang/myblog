from django.db import models

class machine(models.Model):
    machine_type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    buy_time = models.DateTimeField('date buy')


