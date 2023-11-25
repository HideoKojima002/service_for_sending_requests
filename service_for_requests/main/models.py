from django.db import models


class Request(models.Model):
    cadastre_number = models.CharField(max_length=25)
    latitude = models.FloatField()
    longitude = models.FloatField()
    result = models.BooleanField(null=True)

    def __str__(self):
        return f'{self.cadastre_number} ({self.latitude}, {self.longitude})'
