''' digital.py '''

from machine import Pin
    
def write(pin, state):
    write = Pin(pin, Pin.OUT)
    if state == 1:
        write.on()
    elif state == 0:
        write.off()
    #print(pin," is writing", state)  

def on(pin):
    print(pin," is on\n")
    on = Pin(pin, Pin.OUT)
    on.on()
   
def off(pin):
    print(pin," is off\n")
    off = Pin(pin, Pin.OUT)
    off.off()
     
def read(pin):
    value = Pin(pin, Pin.IN)
    print(pin, " returns value ", value())
    return(value())    
