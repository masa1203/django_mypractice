# chat\consumers.py

import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("connect")
        self.accept()

    def disconnect(self, close_code):
        print(close_code)
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)
        # 受け取ったmessageをオウム返しする
        self.send(text_data=json.dumps({
            'message': message
        }))
