import serial
import time
import threading

port = "/dev/rfcomm0"
baudrate = 9600

data_buffer =[]
handlers =[]

def send_to_teensy(data):
    data_buffer.append(data)
    print(data_buffer)
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
    print("Starting loop")
    ser = serial.Serial(port,9600)
    #ser.write(str.encode("Start\r\n"))
    while True:
        if ser.in_waiting > 0:
            print("Can read")
            receive_from_teensy(ser)
        if len(data_buffer) > 0:
            print("Data in buffer")
            data = data_buffer.pop()
            print(data)
            data = str(data)
            ser.write(str.encode(data+"\r\n"))
        time.sleep(1)

def init():
    t = threading.Thread(target=start)
    t.start()

if __name__ == "__main__":
    start()