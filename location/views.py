from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Group, UserLocation
from .serializers import GroupSerializer, UserLocationSerializer
from django.contrib.auth.models import User

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_group(request):
    user = request.user
    group_name = request.data.get('name')
    group = Group.objects.create(name=group_name)
    group.users.add(user)
    serializer = GroupSerializer(group)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def share_location(request):
    user = request.user
    group_id = request.data.get('group_id')
    longitude = request.data.get('longitude')
    latitude = request.data.get('latitude')
    group = Group.objects.get(id=group_id)
    location = UserLocation.objects.create(user=user, group=group, location=f'POINT({longitude} {latitude})')
    serializer = UserLocationSerializer(location)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_group_locations(request, group_id):
    group = Group.objects.get(id=group_id)
    locations = UserLocation.objects.filter(group=group)
    serializer = UserLocationSerializer(locations, many=True)
    return Response(serializer.data)
