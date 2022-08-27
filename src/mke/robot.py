'''robot.py'''

from machine import Pin, I2C

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400_000)

def transmit(address, mode, index, pwm, direction):         
    checkSum = address + mode + index + pwm + direction
    mylist=[address, mode, index, pwm, direction, checkSum]
    motor = bytearray(mylist)
    i2c.writeto(0x40,motor)

def moveForward(speed):
    transmit(0x40, 1, 1, speed, 1)
    transmit(0x40, 1, 0, speed, 1)
    
def moveBackward(speed):
    transmit(0x40, 1, 1, speed, 0)
    transmit(0x40, 1, 0, speed, 0)
    
def turnRight(speed):
    transmit(0x40, 1, 1, speed, 1)
    transmit(0x40, 1, 0, speed, 0)
    
def turnLeft(speed):
    transmit(0x40, 1, 1, speed, 0)
    transmit(0x40, 1, 0, speed, 1)
    
def stop():
    transmit(0x40, 1, 1, 0, 0)
    transmit(0x40, 1, 0, 0, 1)
