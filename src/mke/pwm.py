''' pwm.py '''

from machine import Pin, PWM
from time import sleep

D9 = PWM(Pin(9))
D10 = PWM(Pin(10))
D11 = PWM(Pin(11))

D9.freq(1000)
D10.freq(1000)
D11.freq(1000)

def write(pin, duty):
    if pin == 9:
        D9.duty_u16(duty)
    elif pin == 10:
        D10.duty_u16(duty)
    elif pin == 11:
        D11.duty_u16(duty)
