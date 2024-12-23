from rest_framework import serializers
from .models import Group, UserLocation
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_gis.fields import PointField

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class GroupSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    
    class Meta:
        model = Group
        fields = ['id', 'name', 'users']

class UserLocationSerializer(serializers.ModelSerializer):
    location = PointField()

    class Meta:
        model = UserLocation
        fields = ['user', 'group', 'location', 'timestamp']
