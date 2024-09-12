from channels.generic.websocket import websocketConsumer
import json
from asgiref.sync import async_to_sync



class chatconsumers(websocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.group_name = 'room_%' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
self.group_name,
self.channel_name

        )
        self.accept()
        data={'type':'connected'}

        self.send(text_data=json.dumps(

            { 'plsu'}
        ))


    def receive(self,text_data):
        pass


    def disconnect(self, close_code):
        pass
           