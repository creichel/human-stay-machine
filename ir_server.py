import RPi.GPIO as GPIO
import time

#### SETUP PROCEDURE

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Inputs
# 13: Left
# 19: Right
gpio_ins = [13, 19]

for gpio_in in gpio_ins:
    GPIO.setup(gpio_in, GPIO.IN)

# Outputs
# 20: Green
# 21: Red
gpio_outs = [20, 21]

for gpio_out in gpio_outs:
    GPIO.setup(gpio_out, GPIO.OUT)

#### CODE

# First: Blink 3 Times red, green

for i in range(0,6):
    if i % 2 == 1:
        GPIO.output(gpio_outs[0], GPIO.HIGH)
        GPIO.output(gpio_outs[1], GPIO.LOW)
        print("Turn on green")
    else:
        GPIO.output(gpio_outs[1], GPIO.HIGH)
        GPIO.output(gpio_outs[0], GPIO.LOW)
        print("Turn on green")
    
    time.sleep(1)

# Start motion detection - First: simply use left for green, right for red

while True:
    for gpio_in in gpio_ins:
        i = GPIO.input(gpio_in)

        if i == 1:
            print('found intruder on input %s' % (gpio_in))
            GPIO.output(gpio_outs[i], GPIO.HIGH)
        else: 
            GPIO.output(gpio_outs[i], GPIO.LOW)

        time.sleep(1)