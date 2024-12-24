import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import UserLocation
from .serializers import UserLocationSerializer

class LocationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        self.group_group_name = f'location_{self.group_name}'
        await self.channel_layer.group_add(
            self.group_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        group_id = data['group_id']
        locations = UserLocation.objects.filter(group_id=group_id)
        serializer = UserLocationSerializer(locations, many=True)
        await self.channel_layer.group_send(
            self.group_group_name,
            {
                'type': 'send_location_update',
                'locations': serializer.data
            }
        )

    async def send_location_update(self, event):
        locations = event['locations']
        await self.send(text_data=json.dumps({
            'locations': locations
        }))
