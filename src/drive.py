import sys
import termios
import time
import tty

import RPi.GPIO as gpio

in1 = 23
in2 = 24
in3 = 5
in4 = 6
en1 = 25
en2 = 13

def init():
    gpio.setmode(gpio.BCM)

    # servo
    gpio.setup(en2, gpio.OUT)
    gpio.setup(in3, gpio.OUT)
    gpio.setup(in4, gpio.OUT)

    # motor
    gpio.setup(en1, gpio.OUT)
    gpio.setup(in1, gpio.OUT)
    gpio.setup(in2, gpio.OUT)


def forward():
    gpio.output(in1, gpio.HIGH)
    gpio.output(in2, gpio.LOW)
    motor.ChangeDutyCycle(80)


def reverse():
    gpio.output(in1, gpio.LOW)
    gpio.output(in2, gpio.HIGH)
    motor.ChangeDutyCycle(80)


def steer(angle):
    if angle == 'left':
	gpio.output(in3, gpio.LOW)
	gpio.output(in4, gpio.HIGH)
	servo.ChangeDutyCycle(100)
    if angle == 'right':
        gpio.output(in3, gpio.HIGH)
	gpio.output(in4, gpio.LOW)
	servo.ChangeDutyCycle(100)
    if angle == 'center':
        gpio.output(in3, gpio.LOW)
	gpio.output(in4, gpio.LOW)


def getKey():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    ch = ''
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


# main loop
print('w/s: acceleration')
print('a/d: steering')
print('q: exit')

init()
motor = gpio.PWM(en1, 100)
servo = gpio.PWM(en2, 100)
motor.start(0)
servo.start(0)

while 1 == 1:
    key = getKey()

    if key == 'w':
        forward()
    if key == 's':
        reverse()
    if key == 'a':
        steer('left')
    if key == 'd':
        steer('right')
    if key == 'q':
        print('\nExiting')
        break
    if key == 'f':
	servo.ChangeDutyCycle(0)
	motor.ChangeDutyCycle(0)

    time.sleep(0.1)

gpio.cleanup()

