# Python Import:
import json

# Django Import:
from channels.generic.websocket import AsyncWebsocketConsumer


# Consumers classes:
class CollectConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.channel_layer.group_add('collect', self.channel_name)
        await self.accept()

    async def send_collect(self, event):
        text_message = event['text']
        await self.send(text_message)


class CollectDataConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.channel_layer.group_add('collect_data', self.channel_name)
        await self.accept()

    async def send_collect(self, event):
        text_message = event['text']
        await self.send(text_message)


class LoggerConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.channel_layer.group_add('logger', self.channel_name)
        await self.accept()

    async def send_collect(self, event):
        text_message = event['text']
        await self.send(text_message)



class StatusConsumer(AsyncWebsocketConsumer):
    
    # Join to channel group:
    async def connect(self):
        self.group_name = 'status_update'
        # Join to channel group:
        await self.channel_layer.group_add(
            self.group_name, self.channel_name)
        await self.accept()
    
    # Leave to channel group:
    async def disconnect(self, event):
        # Leave to channel group:
        await self.channel_layer.group_discard(
            self.group_name, self.channel_name)

    # Receive message from group:
    async def send_collect(self, event):
        # Convert Python dictionary into Json:
        json_message = json.dumps(event)
        # Send message to channel:
        await self.send(json_message)
    
    # # Receive message from websocket:
    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #     # Create event dictionary:
    #     event = {
    #         'type': 'send_message',
    #         'message': message,
    #     }
    #     # Receive message from websocket:
    #     await self.channel_layer.group_send(self.group_name, event)
    
    # # Receive message from group:
    # async def send_message(self, event):
    #     message = event['message']
    #     # Receive message from group:
    #     await self.send(text_data=json.dumps({'message': message}))
