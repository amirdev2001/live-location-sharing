from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models as gis_models

class Group(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='groups')
    
    def __str__(self):
        return self.name

class UserLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='locations', on_delete=models.CASCADE)
    location = gis_models.PointField()  # Store location as Point (longitude, latitude)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s location"