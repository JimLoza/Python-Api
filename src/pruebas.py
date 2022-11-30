import serial
import requests
import time

ser = serial.Serial('COM14', 9600, timeout = 1)


while True:
    time.sleep(5)
    lec = float(ser.readline().decode())
    req = requests.post('http://localhost:5000/quality', json={'data': lec})
    print(lec)
    print(req.json())

ser.close()