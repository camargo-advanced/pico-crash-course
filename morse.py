# https://www.youtube.com/watch?v=Tb4iT2pMXoM

import machine
import time

# Configure the LED pin
led = machine.Pin(15, machine.Pin.OUT)  # Pin for the LED

# Function to represent a dot (.)
def dot(led):
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)

# Function to represent a dash (-)
def dash(led):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.2)

# Morse code dictionary for letters and numbers
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----'
}

# Function to represent a letter or number in Morse code
def morse_character(character):
    if character == ' ':
        # Pause between words
        time.sleep(1)
    else:
        for symbol in morse_code[character]:
            if symbol == '.':
                dot(led)
            elif symbol == '-':
                dash(led)
            # Pause between dots and dashes
            time.sleep(0.2)

# Message to be displayed
message = "HELLO WORLD"

# Convert the message to uppercase (Morse code is usually in uppercase)
message = message.upper()

# Loop to go through each character in the message
for character in message:
    morse_character(character)

# Final pause
time.sleep(1)
