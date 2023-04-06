import pwmio
import board
import time

led = pwmio.PWMOut(board.D12)
while True:
    led.duty_cycle = 2 ** 15