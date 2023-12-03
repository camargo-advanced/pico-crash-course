from machine import Pin, ADC
from time import sleep_ms

MAX_ADC_VALUE = 65535

leds = [Pin(13, Pin.OUT), Pin(14, Pin.OUT), Pin(15, Pin.OUT)]
pot = ADC(Pin(26))

while True:
    frequency_hz = int(pot.read_u16() / (MAX_ADC_VALUE/50)) + 1                                                                                                       
    period_ms = int((1000/frequency_hz) / (len(leds)*2)) 
    for led in leds:
        led.high()
        sleep_ms(period_ms)
        led.low()
        sleep_ms(period_ms)