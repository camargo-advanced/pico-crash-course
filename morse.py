from machine import Pin, Timer
from time import sleep_ms

# Configurando o pino 15 como saída para controlar o LED.
led = Pin(15, Pin.OUT)

# Dicionário que relaciona letras e números ao código Morse.
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
     '9': '----.', '0': '-----'
}

# Função que pisca o LED para representar o código Morse.
def flash_morse_code(morse):
    for char in morse:
        if char == '.':
            led.on()  # Liga o LED para representar um ponto.
            sleep_ms(200)  # Mantém o LED aceso por 200 milissegundos (0.2 segundos).
        elif char == '-':
            led.on()  # Liga o LED para representar um traço.
            sleep_ms(600)  # Mantém o LED aceso por 600 milissegundos (0.6 segundos).
        led.off()  # Desliga o LED após o ponto ou traço.
        sleep_ms(200)  # Mantém o LED apagado por 200 milissegundos (0.2 segundos).

# Função que converte texto em código Morse.
def text_to_morse(text):
    morse = ""
    for char in text:
        if char.upper() in morse_code:
            morse += morse_code[char.upper()] + " "
        else:
            morse += " "
    return morse

# Converte o texto "Hello World" em código Morse e imprime.
code = text_to_morse("Hello World")
print("Morse Code:", code)

# Piscando o LED para representar o código Morse.
flash_morse_code(code)