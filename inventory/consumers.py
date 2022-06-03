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
