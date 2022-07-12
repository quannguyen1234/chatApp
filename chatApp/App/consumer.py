import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.http import HttpResponse
import requests 

class chatConsumer(WebsocketConsumer):
    def connect(self):
        print("connected!")
        print("channel",self.channel_name)     
        self.accept()
        self.send(
            text_data=json.dumps({
                'message':'thanh cong',
                'channelname_back':self.channel_name
            })
        )
    
    def receive(self, text_data=None):
        
        print("recived!",self.channel_name) 
        text_data_json=json.loads(text_data)
        type_message=text_data_json['type']
        
        if type_message=='join_room_type':    
            async_to_sync(self.channel_layer.group_add)(
                text_data_json['data']['room_id'], 
                self.channel_name
            )
            
        if type_message=='chat_type':
            message=text_data_json['data']['message']
            room_id=text_data_json['data']['room_id']
            
            json_data={
                'type':'chat_type',
                'message':message,
                'channelname_back':self.channel_name,
            }
            async_to_sync(self.channel_layer.group_send)(
                room_id,
                {   
                    'type':'chat_message',
                    'data':json_data,
                }
            )   
     
    def disconnect(self, code):
        # return      
        pass
    
       
    def chat_message(self,event):
        data=event['data']
        data=json.dumps(
            data
        )
        self.send(
            text_data=data
        )
        print("send:",data)
        