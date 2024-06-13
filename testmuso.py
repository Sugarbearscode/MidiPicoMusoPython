from machine import Pin,UART
import time
uart = UART(0, baudrate=31250, tx=Pin(0), rx=Pin(1)) 
uart.init(bits=8, parity=None, stop=1)
led = Pin("LED", Pin.OUT)
note=24
while True:
    midimessage = bytearray([0x90, note, 64]) 
    uart.write(midimessage)
    led.toggle()
    midimessage = bytearray([0x90, note, 0]) 
    uart.write(midimessage)
    time.sleep(0.125)
    note+=2
    if note > 84:
        note=24
