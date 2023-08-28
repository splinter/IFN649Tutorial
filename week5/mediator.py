import mqtt_proxy
import edge_proxy
import logging

def from_edge(str):
    logging.info("Recieved message from edge %s", str)
    to_mb(str) 
    return

def to_edge(str):
    logging.info("Sending message to edge %s", str)
    edge_proxy.send_to_teensy(str)
    return

def to_mb(str):
    mqtt_proxy.send(mqtt_proxy.DATA_SOIL_TOPIC,str)
    return

def from_mb(str):
    logging.info("Recieved message from mb: %s", str)
    to_edge(str)
    return


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    edge_proxy.init()
    edge_proxy.register(from_edge)

    mqtt_proxy.init()
    mqtt_proxy.register(mqtt_proxy.CONTROL_TOPIC, from_mb)

