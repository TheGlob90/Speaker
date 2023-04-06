import digitalio
import board
import time

led = digitalio.DigitalInOut(board.D17)
while True:
    led.direction = digitalio.Direction.OUTPUT