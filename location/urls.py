from django.urls import path
from . import views

urlpatterns = [
    path('create-group/', views.create_group, name='create_group'),
    path('share-location/', views.share_location, name='share_location'),
    path('group/<int:group_id>/locations/', views.get_group_locations, name='get_group_locations'),
]
