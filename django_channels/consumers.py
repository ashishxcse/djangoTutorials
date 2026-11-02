from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        print("connect...", event)
        self.send({
            'type': 'websocket.accept'
        })
        
    def websocket_receive(self, event):
        print("recieve...", event['text'])
        self.send({
            'type':'websocket.send',
            'text':'from server .....'
            
        })
        
    def websocket_disconnect(self, event):
        print("disconnect...", event)
        raise StopConsumer()
    
    
    
class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        print("connect...", event)
        await self.send({
            'type': 'websocket.accept'
        })
        
    async def websocket_receive(self, event):
        print("recieve...", event['text'])
        await self.send({
            'type':'websocket.send',
            'text':'from server .....'
            
        })
        
    async def websocket_disconnect(self, event):
        print("disconnect...", event)
        raise StopConsumer()