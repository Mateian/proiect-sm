import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BOARD)
channel = 5
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    print('foc')

try:
    while True:
        if GPIO.input(channel) == 0:
            with open("/var/www/python/stare.txt", "w") as f:
                f.write("Foc detectat!")
                print('foc')
        else:
            with open("/var/www/python/stare.txt", "w") as f:
                f.write("")
        time.sleep(0.5)
except KeyboardInterrupt:
    print('oprire')
finally:
    GPIO.cleanup()
