from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from time import sleep_ms

# Configura sensor de temperatura
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

# Configuração do I2C para se comunicar com o módulo OLED
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)  
display = SSD1306_I2C(128, 64, i2c, 0x3C)
sleep_ms(1000)  # Aguarda configuração ser aplicada

while True:
    # Lê sensor de temperatura do Pico e calcula temperatura
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    formatted_temperature = f"{temperature:.1f}"

    # Escreve no display
    display.fill(0)
    display.text("Temperature (C)", 5, 5)
    display.text(formatted_temperature, 50, 27)
    display.show()
    
    sleep_ms(500)  # Aguarda meio segundo