import RPi.GPIO as GPIO
import time
import lcd_16x2 as LCD
import sys
from datetime import datetime
import os

def init_program():
    with open("/var/www/python/stop.txt", "w") as f:
        f.write("false")

init_program()

# GPIO setup
GPIO.setmode(GPIO.BOARD)
flame_channel = 3
smoke_channel = 5
status_channel = 40
GPIO.setup(flame_channel, GPIO.IN)
GPIO.setup(smoke_channel, GPIO.IN)
GPIO.setup(status_channel, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(LCD.LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD.LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD.LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD.LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD.LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD.LCD_D7, GPIO.OUT) # DB7

LCD.lcd_init()

GPIO.output(status_channel, GPIO.HIGH)
LCD.lcd_clear()
LCD.lcd_string("Alarma pornita.", LCD.LCD_LINE_1)
time.sleep(2)
LCD.lcd_string("", LCD.LCD_LINE_1)
time.sleep(1)

first_lcd_text = ""
second_lcd_text = ""

if(len(sys.argv) >= 2):
    lcd_text = ""
    for i in range(1, len(sys.argv)):
        lcd_text += sys.argv[i] + " "
        if len(lcd_text) > 16:
            first_lcd_text = lcd_text[:16]
            second_lcd_text = lcd_text[16:len(lcd_text)]
        else:
            first_lcd_text = lcd_text[:15]
            second_lcd_text = ""

def is_stopped():
    with open("/var/www/python/stop.txt") as f:
        stopped = f.read()
        if stopped == "true":
            return True
    return False

def is_fire():
    return not GPIO.input(flame_channel)

try:
    while True:
        if is_stopped() == True:
            break
        if is_fire():
            with open("/var/www/python/stare.txt", "w") as f:
                f.write("Foc detectat!")
            if(len(sys.argv) >= 2):
                LCD.lcd_string(first_lcd_text, LCD.LCD_LINE_1)
                LCD.lcd_string(second_lcd_text, LCD.LCD_LINE_2)
                GPIO.output(status_channel, GPIO.LOW)
                time.sleep(0.25)
                GPIO.output(status_channel, GPIO.HIGH)
                time.sleep(0.25)
                GPIO.output(status_channel, GPIO.LOW)
                LCD.lcd_clear()
                time.sleep(0.25)
                GPIO.output(status_channel, GPIO.HIGH)
                time.sleep(0.25)
            else:
                LCD.lcd_string("   Incendiu!", LCD.LCD_LINE_1)
                LCD.lcd_string(" Spre evacuare! ", LCD.LCD_LINE_2)
                
                GPIO.output(status_channel, GPIO.LOW)
                time.sleep(0.25)
                GPIO.output(status_channel, GPIO.HIGH)
                time.sleep(0.25)
                GPIO.output(status_channel, GPIO.LOW)
                LCD.lcd_clear()
                time.sleep(0.25)
                GPIO.output(status_channel, GPIO.HIGH)
                time.sleep(0.25)
                                
        else:
            with open("/var/www/python/stare.txt", "w") as f:
                    f.write("Totul este in regula.")
            LCD.lcd_string(str(datetime.now().strftime("%H:%M:%S %d-%m")), LCD.LCD_LINE_2)
            time.sleep(0.5)
except KeyboardInterrupt:
    print("\nParasire program...\n")
finally:
    LCD.lcd_clear()
    LCD.lcd_string("Alarma oprita.", LCD.LCD_LINE_1)
    time.sleep(1)
    LCD.lcd_clear()
    GPIO.output(status_channel, GPIO.LOW)

    GPIO.cleanup()
