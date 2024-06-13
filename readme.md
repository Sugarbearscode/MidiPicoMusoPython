If you want a Midi to CV convert then you can worse than this https://midimuso.co.uk/index.php/product/cv-12-full-kit/ you will have to build it yourself though. 

Example code for sending midi notes 

Ascending Notes
# ++++++++++++++ program starts here ++++++++++++ from machine import Pin,UART
import time
uart = UART(0, baudrate=31250, tx=Pin(0), rx=Pin(1)) uart.init(bits=8, parity=None, stop=1)
led = Pin("LED", Pin.OUT) note = 24
while True:
midimessage = bytearray([0x90, note, 64]) uart.write(midimessage)
led.toggle()
midimessage = bytearray([0x90, note, 0]) uart.write(midimessage)
time.sleep(0.125)
note+=2
if note > 84:
note=24
# ++++++++++++++ program ends here ++++++++++++

and a midi echo (read from MIDI IN and write that to MIDI OUT 

MIDI echo
# ++++++++++++++ program starts here ++++++++++++ from machine import Pin,UART
import time
uart1 = UART(0, baudrate=31250, tx=Pin(0), rx=Pin(1)) uart2 = UART(1, baudrate=31250, tx=Pin(4), rx=Pin(5)) uart1.init(bits=8, parity=None, stop=1)
led = Pin("LED", Pin.OUT)
while True:
if uart1.any() > 0:
data = uart1.read(1) uart1.write(data) uart2.write(data) led.toggle()
# ++++++++++++++ program ends here ++++++++++++
