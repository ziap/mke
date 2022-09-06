''' analog.py '''

from machine import Pin, ADC            #importing Pin and ADC class
voltage_offset = 3.3

def set_voltage(voltage):
    voltage_offset = voltage
    print(voltage_offset)

def read(pin):
    analogPin = ADC(pin)
    analogValue = analogPin.read_u16()
    print("analog value at pin ", pin, " is ", analogValue)
    return analogValue

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def read_percent(pin):
    analogPin = ADC(pin)
    analogValue = map_range(analogPin.read_u16(), 0, 65536, 0, 100)
    print("analog value at pin ", pin, " is ", analogValue)
    return analogValue

def read_voltage(pin):
    analogPin = ADC(pin)
    analogValue = map_range(analogPin.read_u16(), 0, 65536, 0, 3.30)
    print("analog value at pin ", pin, " is ", analogValue)
    return analogValue
