import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']  # Get room_name from URL
        self.room_group_name = f'chat_{self.room_name}'

        # Join the chat room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the chat room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive message from WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = self.scope['user'].username  # Get the username of the sender

        # Save message to the database
        receiver_username = self.room_name  # Assume room_name is the receiver
        receiver = await database_sync_to_async(User.objects.get)(username=receiver_username)
        await database_sync_to_async(Message.objects.create)(
            sender=self.scope['user'],
            receiver=receiver,
            content=message
        )

        # Send message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'sender': sender,
                'message': message
            }
        )

    # Receive message from group
    async def chat_message(self, event):
        sender = event['sender']
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'sender': sender,
            'message': message
        }))
