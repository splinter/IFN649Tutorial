import mqtt_proxy
# import sensor_proxy
import logging

def from_edge(str):
    to_mb(str)
    return

def to_edge(str):
    # sensor_proxy.send_to_teensy(str)
    return

def to_mb(str):
    mqtt_proxy.send(str)
    return

def from_mb(str):
    logging.info("Recieved message from mb: %s", str)
    to_edge(str)
    return


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    #sensor_proxy.register(from_edge)

    mqtt_proxy.init()
    mqtt_proxy.register(mqtt_proxy.CONTROL_TOPIC, from_mb)

