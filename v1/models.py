from django.contrib.gis.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    location = models.PointField()


    def __str__(self):
        return self.name
