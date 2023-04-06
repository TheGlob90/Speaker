import digitalio
import board
import time

led = digitalio.DigitalInOut(board.D17)
led.direction = digitalio.Direction.OUTPUT
while True:
    led.value = True