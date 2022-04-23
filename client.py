import RPi.GPIO as GPIO
from ConOut import ConOut
from time import sleep
import socket
import random


def swap(controllers):
    nums = list(range(0, len(controllers)))
    random.shuffle(nums)
    for controller in controllers:
        controller.set_out(nums.pop())

SA1 = 23
SA2 = 33
SA3 = 29
SA4 = 31

A1 = 8
B1 = 10
EN1 = 24

A2 = 12
B2 = 16
EN2 = 32

A3 = 18
B3 = 22
EN3 = 36

A4 = 26
B4 = 35
EN4 = 38

GPIO.setmode(GPIO.BOARD)

GPIO.setup(SA1, GPIO.OUT)
GPIO.setup(SA2, GPIO.OUT)
GPIO.setup(SA3, GPIO.OUT)
GPIO.setup(SA4, GPIO.OUT)

GPIO.output(SA1, GPIO.LOW)
GPIO.output(SA2, GPIO.LOW)
GPIO.output(SA3, GPIO.LOW)
GPIO.output(SA4, GPIO.LOW)

out1 = ConOut(A1, B1, EN1)
out2 = ConOut(A2, B2, EN2)
out3 = ConOut(A3, B3, EN3)
out4 = ConOut(A4, B4, EN4)

out1.set_out(0)
out2.set_out(1)
out3.set_out(2)
out4.set_out(3)

mode = 'Normal'

# Create a socket object
s = socket.socket()        

# Define the port on which you want to connect
port = 12345   
ip = socket.gethostbyname('Archimedes')
# connect to the server on local computer
s.connect((ip, port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())

while(True):
    if mode == 'Normal':
        sleep(5)
        swap([out1, out2, out3, out4])
    

GPIO.cleanup()