import lcd_16x2 as LCD
import RPi.GPIO as GPIO
import time
import sys

lcd_text = ""

if(len(sys.argv) >= 2):
    for i in range(1, len(sys.argv)):
        lcd_text += sys.argv[i] + " "
        if len(lcd_text) > 16:
            first_lcd_text = lcd_text[:16]
            second_lcd_text = lcd_text[16:len(lcd_text)]
        else:
            first_lcd_text = lcd_text[:15]
            second_lcd_text = ""

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LCD.LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD.LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD.LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD.LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD.LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD.LCD_D7, GPIO.OUT) # DB7

LCD.lcd_init()

LCD.lcd_string(lcd_text, LCD.LCD_LINE_1);

print("text schimbat")

time.sleep(5);

LCD.lcd_clear()

GPIO.cleanup()
