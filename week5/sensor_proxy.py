import serial
import time
import threading

port = "/dev/rfcomm0"
baudrate = 9600

data_buffer =[]
handlers =[]

def send_to_teensy(message):
    return

def register(handler):
    handlers.append(handler)

def receive_from_teensy(ser):
    data = ser.readline()
    processed = data.decode("utf-8").strip("\r\n")
    print(processed)
    for handler in handlers:
        handler(data)
    return

def establish_connection():
    serial = serial
    return

def start():
    ser = serial.Serial(port,9600)
    ser.write(str.encode("Start\r\n"))
    while True:
        if ser.in_waiting > 0:
            print("Can read")
            receive_from_teensy(ser)
        if len(data_buffer) > 1:
            send_to_teensy(ser)
        time.sleep(1)

if __name__ == "__main__":
    start()