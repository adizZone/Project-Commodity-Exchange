from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.contrib.auth.models import User
from .models import ChatBox
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.sender = self.scope['user']
        self.room_name = self.scope['url_route']['kwargs'].get('room_name')
        self.rec = self.room_name.split('-')
        self.receiver = await self.get_receiver(self.rec[-1])

        self.group_name = f"chat_{self.room_name}"

        # Add the consumer to the group
        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    @database_sync_to_async
    def get_receiver(self, receiver_id):
        return User.objects.get(id=receiver_id)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message']
        
        message = await self.create_message(message_content)

        message_data = {
            'id': message.id,
            'message': message.message,
            'sender_id': self.sender.id,
            'sender_username': self.sender.username,
        }

        # Send message to individual
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message_data,
            }
        )
        

    @database_sync_to_async
    def create_message(self, message_content):
        message = ChatBox.objects.create(sender=self.sender, receiver=self.rec[-1], message=message_content, room=self.room_name)
        return message

    async def send_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))
