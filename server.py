import socket
import threading

global t_lock
global c

def checkIncoming():
    global t_lock
    global c
    print("Starting threading...")
    while 1:
        data = c.recv(1024)
        data = data.decode()

        if not data:
            continue
        with t_lock:
            print(data)
            t_lock.notify()

t_lock = threading.Condition()

# next create a socket object
s = socket.socket()		
print ("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345			

s.bind(('', port))		
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)	
print ("socket is listening")		

# Establish connection with client.
c, addr = s.accept()	
print ('Got connection from', addr )

# send a thank you message to the client. encoding to send byte type.
c.send('Thank you for connecting'.encode())

Central = threading.Thread(target=checkIncoming)
Central.daemon = True
Central.start()

# a forever loop until we interrupt it or
# an error occurs
msg = ""
while msg != "Exit":
    msg = input()
    c.send(msg.encode())
