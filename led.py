import pwmio
import board
import time

led = pwmio.PWMOut(board.D18)
while True:
    led.duty_cycle = 2 ** 15