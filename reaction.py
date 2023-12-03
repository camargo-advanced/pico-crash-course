from machine import Pin
from time import sleep_ms, ticks_ms, ticks_diff
from random import randint

# Configuração dos pinos
led = Pin(15, Pin.OUT)
right_button = Pin(16, Pin.IN, Pin.PULL_DOWN)
left_button = Pin(17, Pin.IN, Pin.PULL_DOWN)

pressed_button = None

# Identifica botão pressionado
def button_pressed(pin):
    right_button.irq(handler=None)
    left_button.irq(handler=None)
    global pressed_button
    pressed_button = pin
    
# Se jogador pressionar botão durante a espera, perde o jogo
def pressed_in_waiting():
    waiting_time = randint(1, 5) * 1000

    led.high()
    timer_start = ticks_ms()
    
    # Aguarda jogador pressionar o botão
    while ticks_diff(ticks_ms(), timer_start) < waiting_time:
        if pressed_button is not None: break
        sleep_ms(5)
        
    if pressed_button is left_button:
        print("Left Player lost!")
    elif pressed_button is right_button:
        print("Right Player lost!")
    
    led.low()
    
    return pressed_button
    
# Função principal do jogo
def main_game():
    # Configura função de interrupção para tratamento dos botões
    left_button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)
    right_button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)

    if pressed_in_waiting() is None:
        timer_start = ticks_ms()

        # Aguarda jogador pressionar o botão
        while pressed_button is None:
            sleep_ms(5)
                
        if pressed_button is left_button:
            print("Left Player wins!")
        elif pressed_button is right_button:
            print("Right Player wins!")
            
        timer_reaction = ticks_diff(ticks_ms(), timer_start)
        print("Time to react: " + str(timer_reaction) + " milliseconds!")

main_game()