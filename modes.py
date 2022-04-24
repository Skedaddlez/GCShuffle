import ConOut
from time import time
import random
from socket import socket

def swap(controllers, nums=None):
    if nums is None:
        nums = list(range(0, len(controllers)))
    random.shuffle(nums)
    for controller in controllers:
        controller.set_out(nums.pop())

class Normal:
    def __init__(self, out1, out2, out3, out4, sock):
        self.out1 = out1
        self.out2 = out2
        self.out3 = out3
        self.out4 = out4
        self.socket = sock
        pass

    def initialise(self):
        self.out1.set_out(0)
        self.out2.set_out(1)
        self.out3.set_out(2)
        self.out4.set_out(3)

    def loop(self):
        pass

class Shuffle2P:
    def __init__(self, out1, out2, out3, out4, sock):
        self.out1 = out1
        self.out2 = out2
        self.out3 = out3
        self.out4 = out4
        self.sock = sock
        self.last_swap = time()
        self.time_to_next_swap = random.randint(2,100)
        pass

    def initialise(self):
        self.out1.set_out(0)
        self.out2.set_out(1)
        self.out3.set_out(2)
        self.out4.set_out(3)

        self.out3.enable(False)
        self.out4.enable(False)

    def loop(self):
        if time() - self.last_swap > self.time_to_next_swap:
            swap([self.out1, self.out2])
            self.last_swap = time()
            self.time_to_next_swap = random.randint(2, 100)
            self.sock.sendall('Swapped'.encode())

class Shuffle3P:
    def __init__(self, out1, out2, out3, out4, sock):
        self.out1 = out1
        self.out2 = out2
        self.out3 = out3
        self.out4 = out4
        self.sock = sock
        self.last_swap = time()
        self.time_to_next_swap = random.randint(2, 100)
        pass

    def initialise(self):
        self.out1.set_out(0)
        self.out2.set_out(1)
        self.out3.set_out(2)
        self.out4.set_out(3)

        self.out4.enable(False)

    def loop(self):
        if time() - self.last_swap > self.time_to_next_swap:
            swap([self.out1, self.out2, self.out3])
            self.last_swap = time()
            self.time_to_next_swap = random.randint(2, 100)
            self.sock.sendall('Swapped'.encode())

class Shuffle4P:
    def __init__(self, out1, out2, out3, out4, sock):
        self.out1 = out1
        self.out2 = out2
        self.out3 = out3
        self.out4 = out4
        self.sock = sock
        self.last_swap = time()
        self.time_to_next_swap = random.randint(2, 100)
        pass

    def initialise(self):
        self.out1.set_out(0)
        self.out2.set_out(1)
        self.out3.set_out(2)
        self.out4.set_out(3)

    def loop(self):
        if time() - self.last_swap > self.time_to_next_swap:
            swap([self.out1, self.out2, self.out3, self.out4])
            self.last_swap = time()
            self.time_to_next_swap = random.randint(2, 100)
            self.sock.sendall('Swapped'.encode())

class Shuffle2P2P:
    def __init__(self, out1, out2, out3, out4, sock):
        self.out1 = out1
        self.out2 = out2
        self.out3 = out3
        self.out4 = out4
        self.sock = sock
        self.last_swap = time()
        self.time_to_next_swap = random.randint(2, 100)
        pass

    def initialise(self):
        self.out1.set_out(0)
        self.out2.set_out(1)
        self.out3.set_out(2)
        self.out4.set_out(3)

    def loop(self):
        if time() - self.last_swap > self.time_to_next_swap:
            swap([self.out1, self.out2], [0, 1])
            swap([self.out3, self.out4], [2, 3])
            self.last_swap = time()
            self.time_to_next_swap = random.randint(2, 100)
            self.sock.sendall('Swapped'.encode())

class Shuffle4I1O:
    def __init__(self, out1, out2, out3, out4, sock):
        self.out1 = out1
        self.out2 = out2
        self.out3 = out3
        self.out4 = out4
        self.sock = sock
        self.last_swap = time()
        self.time_to_next_swap = random.randint(2, 100)
        pass

    def initialise(self):
        self.out1.set_out(0)
        self.out2.set_out(1)
        self.out3.set_out(2)
        self.out4.set_out(3)

        self.out2.enable(False)
        self.out3.enable(False)
        self.out4.enable(False)

    def loop(self):
        if time() - self.last_swap > self.time_to_next_swap:
            swap([self.out1, self.out2, self.out3, self.out4])
            self.last_swap = time()
            self.time_to_next_swap = random.randint(2, 100)
            self.sock.sendall('Swapped'.encode())

class Normal1I4O:
    def __init__(self, out1, out2, out3, out4, sock):
        self.out1 = out1
        self.out2 = out2
        self.out3 = out3
        self.out4 = out4
        self.sock = sock
        pass

    def initialise(self):
        self.out1.set_out(0)
        self.out2.set_out(0)
        self.out3.set_out(0)
        self.out4.set_out(0)

    def loop(self):
        pass