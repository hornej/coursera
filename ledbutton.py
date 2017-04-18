import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.IN)

while True:
    input_value = GPIO.input(18)
    
    if input_value == True:
        GPIO.output(16,True)
        while input_value == True:
            input_value = GPIO.input(18)
    else:
        GPIO.output(16,True)
        time.sleep(.2)
        GPIO.output(16,False)
        time.sleep(.2)
        
GPIO.cleanup()
