import RPi.GPIO as GPIO
from ConOut import ConOut
from time import sleep
import socket
import random
import threading

global t_lock
global mode
global s
global modes
modes = ['Normal','3PShuffle', '4PShuffle', 'Exit']


def swap(controllers):
    nums = list(range(0, len(controllers)))
    random.shuffle(nums)
    for controller in controllers:
        controller.set_out(nums.pop())

def checkIncoming():
    global t_lock
    global mode
    global modes
    print("Starting threading...")
    while 1:
        data, addr = s.recvfrom(1024)
        data = data.decode()

        if not data:
            continue
        with t_lock:
            if data in modes:
                mode = data
                print("Mode is now " + mode)
            else:
                print("MSG unknown.")
            t_lock.notify()

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
t_lock = threading.Condition()

# Create a socket object
s = socket.socket()        

# Define the port on which you want to connect
port = 12345   
ip = socket.gethostbyname('Archimedes')
# connect to the server on local computer
s.connect((ip, port))

# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())

Central = threading.Thread(target=checkIncoming)
Central.daemon = True
Central.start()

running = True
while running:
    if mode == 'Normal':
        sleep(0.01)
    elif mode == '3PShuffle':
        sleep(randint(2,100))
        swap([out1, out2, out3])
        s.send('Swapped'.encode())
    elif mode == '4PShuffle':
        sleep(randint(2,100))
        swap([out1, out2, out3, out4])
        s.send('Swapped'.encode())
    elif mode == 'Exit':
        running = False
    

GPIO.cleanup()