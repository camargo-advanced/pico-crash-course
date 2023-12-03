from machine import ADC, Pin
from time import sleep_ms

adc = ADC(Pin(26))

while True:
    print(adc.read_u16())
    time.sleep_ms(5)