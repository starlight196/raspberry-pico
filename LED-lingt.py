from machine import Pin
import time
led=machine.Pin(25,machine.Pin.OUT)

while True:
    led.value(1)
    time.sleep(0.3)
    led.value(0)
    time.sleep(0.3)
