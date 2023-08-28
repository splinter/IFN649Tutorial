import threading
import time
import paho.mqtt.client as mqtt
import logging

mqtt_host="54.242.14.9"

DATA_TEMP_TOPIC = "/data/tuts/sensors/temp"
DATA_SOIL_TOPIC = "/data/tuts/sensors/soil"
CONTROL_TOPIC = "/control"

handlers={}
data=[]

def send(topic,str):
    client.publish(topic,str)
    return

def register(topic, handler):
    logging.info("Subscribing to %s", topic)
    client.subscribe(topic)
    if topic not in handlers:
        handlers[topic] = []
    handlers[topic].append(handler)
    return

def on_message(client,userdata,msg):
    print("Recieved message")
    print(msg.payload)
    for topic in handlers:
        if(topic == msg.topic):
            for handler in handlers[topic]:
                handler(msg.payload)

def on_connect(client, userdata,flags,rc):
    print("Connected")
    logging.info("Successfully connected to mqtt server %s"%(mqtt_host))

def loop_forever():
    client.on_connect = on_connect
    client.on_message = on_message
    port = 1883
    client.connect(mqtt_host,port,60)
    client.subscribe(CONTROL_TOPIC)
    client.loop_forever()


def init():
    global client
    logging.basicConfig()
    client = mqtt.Client()
    # client.on_connect = on_connect
    # client.on_message = on_message
    # port = 1883
    # client.connect(mqtt_host,port,60)
    # client.subscribe("test")
    # client.loop_forever()

    t = threading.Thread(target=loop_forever)
    t.start()
