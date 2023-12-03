from machine import Pin, PWM
from time import sleep_ms

MAX_DUTY_VALUE = 65535 

pwm = PWM(Pin(15))
pwm.freq(500)

frequency_hz = 3
period_ms = int((1/frequency_hz) * 1000)
duty_inc_per_ms = int(MAX_DUTY_VALUE / (period_ms/2))

while True:
    for duty in range(0, MAX_DUTY_VALUE, duty_inc_per_ms):
        pwm.duty_u16(duty)
        sleep_ms(1)

    for duty in range(MAX_DUTY_VALUE, 0, -duty_inc_per_ms):
        pwm.duty_u16(duty)
        sleep_ms(1)