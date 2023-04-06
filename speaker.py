import pwmio
import board
import time

pwm = pwmio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=440)
while True:
    time.sleep(0.2)
    pwm.frequency = 880
    time.sleep(0.1)