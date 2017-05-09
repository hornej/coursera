import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)

led_1 = 16

pwm = GPIO.PWM(led_1,50)
pwm.start(0)

while True:
    
    for i in range(100):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.008)
    time.sleep(.3)
    for i in range(100,0,-1):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.008)
    time.sleep(.3)
