import machine
import time


led = machine.Pin(2, machine.Pin.OUT)
while True:
    time.sleep(.3)
    led.off()
    time.sleep(.1)
    led.on()
