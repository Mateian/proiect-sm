import RPi.GPIO as GPIO
import time

class LCD:
    def __init__(self):
        self.RS = 26
        self.E = 19
        self.D4 = 13
        self.D5 = 6
        self.D6 = 5
        self.D7 = 11
        self.pins = [self.D4, self.D5, self.D6, self.D7]

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RS, GPIO.OUT)
        GPIO.setup(self.E, GPIO.OUT)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

        self.lcd_init()

    def lcd_init(self):
        self.lcd_cmd(0x33)
        self.lcd_cmd(0x32)
        self.lcd_cmd(0x28)
        self.lcd_cmd(0x0C)
        self.lcd_cmd(0x06)
        self.lcd_cmd(0x01)
        time.sleep(0.005)

    def lcd_cmd(self, cmd):
        GPIO.output(self.RS, GPIO.LOW)
        self.lcd_write(cmd)

    def lcd_write_char(self, char):
        GPIO.output(self.RS, GPIO.HIGH)
        self.lcd_write(ord(char))

    def lcd_write(self, data):
        for i in [4, 0]:
            for bit in range(4):
                GPIO.output(self.pins[bit], (data >> (bit + i)) & 0x01)
            self.lcd_toggle_enable()

    def lcd_toggle_enable(self):
        time.sleep(0.0005)
        GPIO.output(self.E, True)
        time.sleep(0.0005)
        GPIO.output(self.E, False)
        time.sleep(0.0005)

    def lcd_string(self, message, line):
        lines = [0x80, 0xC0]
        self.lcd_cmd(lines[line - 1])
        for char in message.ljust(16):
            self.lcd_write_char(char)

    def lcd_clear(self):
        self.lcd_cmd(0x01)

    def cleanup(self):
        GPIO.cleanup()

