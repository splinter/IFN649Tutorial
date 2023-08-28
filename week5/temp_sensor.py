import mqtt_proxy
import sensor_proxy

handlers=[]

def on_data(data):
    if data:
        for handler in handlers:
            handler(data)
        
def init():
    sensor_proxy.register()
    return

def on_update(handler):
    handlers.append(handler)
    return

