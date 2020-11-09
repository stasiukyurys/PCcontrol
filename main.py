import machine
import time
import esp


led = machine.Pin(2, machine.Pin.OUT)
while True:
    time.sleep(2)
    led.off()
    time.sleep(2)
    led.on()
