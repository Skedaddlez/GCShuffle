import RPi.GPIO as GPIO

class ConOut:
    def __init__(self, a, b, en):
        self.a = a
        GPIO.setup(self.a, GPIO.OUT)
        self.b = b
        GPIO.setup(self.b, GPIO.OUT)
        self.en = en
        GPIO.setup(self.en, GPIO.OUT)

    def set_out(self, num):
        bin_num = bin(num)
        a_state = GPIO.HIGH if bin_num[-1] == '1' else GPIO.LOW
        GPIO.output(self.a, a_state)
        b_state = GPIO.HIGH if bin_num[-2] == '1' else GPIO.LOW
        GPIO.output(self.b, b_state)

    def enable(self, state):
        en_state = GPIO.LOW if state else GPIO.HIGH
        GPIO.output(self.en, en_state)