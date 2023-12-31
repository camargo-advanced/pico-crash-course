## Capítulo 12: Projeto Código morse com um Buzzer

Bem-vindos ao incrível mundo da comunicação através do Código Morse com o Raspberry Pi Pico! Neste capítulo, vamos explorar como utilizar um buzzer para criar sons que representam o Código Morse. 

Neste projeto, vamos conectar o buzzer ao Raspberry Pi Pico e utilizar o código Morse para representar mensagens através de luzes e sons. Preparados para decifrar e transmitir mensagens codificadas? Vamos mergulhar nesse fascinante mundo dos sons!

### O que é um Buzzer?

Um Buzzer é um pequeno dispositivo que emite um som quando é alimentado com energia elétrica. É como uma campainha que emite um som quando é ativada. 

Existem dois tipos principais de buzzers:

- Buzzer Ativo: Um buzzer ativo é mais simples de usar. Ele possui um circuito interno que gera um tom específico quando é alimentado com energia. Esse tipo de buzzer sempre emite o mesmo som.

- Buzzer Passivo: Um buzzer passivo é um pouco mais versátil. Ele não possui um circuito interno para gerar um tom específico. Em vez disso, ele emite sons diferentes dependendo do sinal elétrico que recebe. Para fazer um buzzer passivo emitir um som, você precisa conectar e desconectar a energia rapidamente, criando assim diferentes tons.

![Imagem de buzzers passivos](/images/buzzers.jpg "Imagem de buzzers passivos")

Um buzzer passivo pode ser mais interessante para criar diferentes sons ou músicas, já que você pode controlar os tons emitidos por ele através da programação. Isso pode ser feito através do controle da frequência em Hertz usando a função `PWM`. Por exemplo, para gerar a nota musical A4 podemos definir a frequência em 440 Hz.

### Adicionando som ao projeto

Primeiramente conecte o buzzer em circuito. Para fazer isso conecte um fio de conexão ao pino **GP16** do seu pico e conecte a outra ponta dele na perna mais longa do buzzer. A perna mais curta do buzzer deve ser conectada ao terra (GND), o que pode ser feito com um outro fio de conexão. 

A imagem que segue apresenta uma forma de se montar esse cicuito na placa de prototipagem.

![Circuito com 1 LED e 1 Buzzer](/images/morse-buzzer-circuit.png "Circuito com 1 LED e 1 Buzzer")

> **`Importante`**: O buzzer, assim como o LED, possui uma perna mais longa que deve ser conectada a tensão mais alta gerada por um pino do seu pico. Lembre-se de sempre considerar essa regra para não queimar o componente.

Após conectar o buzzer, adicione este código a um novo arquivo no Thonny, salve-o em seu Raspberry Pi Pico como `morse-led-buzzer.py` e depois execute-o. 

Para ver este circuito em funcionamento no simulador Wokwi, clique [aqui](https://wokwi.com/projects/382822078849464321).

```python
from machine import Pin, PWM, Timer
from time import sleep_ms

# Configurando o pino 15 como saída para controlar o LED.
led = Pin(15, Pin.OUT)

# Configurando o pino 16 para controlar o buzzer com PWM
buzzer = PWM(Pin(16))
buzzer.duty_u16(0)  # Desliga o buzzer inicialmente
buzzer.freq(440) 

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

# Função que pisca o LED e emite som para representar o código Morse.
def flash_morse_code(morse):
    for char in morse:
        if char == '.':
            led.on()  
            buzzer.duty_u16(1000)  
            sleep_ms(200)  
        elif char == '-':
            led.on()  
            buzzer.duty_u16(1000)  
            sleep_ms(600)  
        led.off()  
        buzzer.duty_u16(0)  
        sleep_ms(200)  

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
```

Programa 12.1

Vamos desvendar esse código !

```python
from machine import Pin, PWM, Timer
from time import sleep_ms

led = Pin(15, Pin.OUT)

buzzer = PWM(Pin(16))
buzzer.duty_u16(0)  
buzzer.freq(440) 
```

Neste bloco, estamos inicializando o Raspberry Pi Pico para controlar o LED e o buzzer. O pino `15` (GP15) é configurado como saída para o LED e o pino `16` (GP16) é configurado para controlar o buzzer utilizando modulação por largura de pulso (PWM). A frequência do buzzer é ajustada para 440 Hz, que é a frequência aproximada da nota musical **A4** utilizada em código morse.

```python
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    # ... (outros códigos Morse)
    '0': '-----'
}
```

Aqui definimos um dicionário que mapeia letras e números para seus equivalentes em código Morse. Por exemplo, 'A' é representado como '.-'.

```python
def flash_morse_code(morse):
    for char in morse:
        if char == '.':
            led.on()  
            buzzer.duty_u16(1000)  
            sleep_ms(200)  
        elif char == '-':
            led.on()  
            buzzer.duty_u16(1000)  
            sleep_ms(600)  
        led.off()  
        buzzer.duty_u16(0)  
        sleep_ms(200)  
```

Esta função aceita uma sequência de código Morse e a percorre. Para cada caractere (ponto ou traço), ela liga o LED e o buzzer e aguarda o tempo especificado. Em seguida, desliga o LED e o buzzer e espera um curto intervalo antes de passar para o próximo caractere. Para ligar o buzzer definimos alteramos seu ciclo de trabalho (duty cycle) para o valor 1000. Para desligá-lo, alteramos o ciclo de trabalho para 0. O ciclo de trabalho foi explicado anteriormente nesse curso. Consulte a explicação anterior para entender seu funcionamento se necessário.

```python
def text_to_morse(text):
    morse = ""
    for char in text:
        if char.upper() in morse_code:
            morse += morse_code[char.upper()] + " "
        else:
            morse += " "
    return morse
```

Esta função aceita uma string de texto e a converte em código Morse usando o dicionário `morse_code`. Se um caractere não estiver no dicionário, ele é substituído por um espaço.

```python
code = text_to_morse("Hello World")
print("Morse Code:", code)

flash_morse_code(code)
```

Aqui, o texto 'Hello World' é convertido em código Morse e exibido. Em seguida, a função `flash_morse_code` é chamada para piscar o LED e emitir som de acordo com o código Morse gerado.

Altere o texto para outras palavras e frases e veja o resultado. Por exemplo, você pode mudar para SOS e dessa forma estar preparado para se comunicar em uma situação de emergência com uma lanterna!

### Exercícios

#### Exercício 12.1: Sinais de Pausa

Acrescente um novo caractere, como o ponto-e-vírgula (;), ao dicionário `morse_code` e defina sua representação em Código Morse como uma pausa longa entre palavras. Modifique um texto para incluir essa pausa e observe como ela é representada tanto no LED quanto no buzzer.

#### Exercício 12.2: Frases Longas

Altere o texto fornecido para uma frase mais longa, como "Hello from the Raspberry Pi World", e observe como a tradução em Código Morse é transmitida pelo LED e buzzer. Experimente enviar mensagens mais complexas e verifique como o código representa cada letra e palavra na comunicação em Código Morse.

#### Exercício 12.3: Sons Personalizados

Modifique a função `flash_morse_code` para criar tons diferentes no buzzer para representar os pontos e traços do Código Morse. Experimente usar frequências diferentes para cada ponto e traço. Por exemplo, faça o ponto ter uma frequência de 1000 Hz e o traço de 2000 Hz.

### Conclusão

Parabéns por explorar o projeto emocionante de comunicação através do Código Morse com o Raspberry Pi Pico e um buzzer! Durante este capítulo, você descobriu como um pequeno dispositivo pode ser programado para emitir sons representando letras e números conforme o Código Morse.

Através da programação do Raspberry Pi Pico, você pôde controlar o buzzer para emitir tons curtos e longos, correspondentes aos sinais de ponto e traço do Código Morse. Com isso, criamos uma forma de comunicação que transcendeu a simples escrita, utilizando luzes e sons para transmitir mensagens.

O universo do Raspberry Pi Pico e da comunicação por Código Morse está repleto de possibilidades. Continue explorando, experimentando e se desafiando com novos projetos. Quem sabe você não cria a próxima grande inovação na área da comunicação utilizando essas incríveis ferramentas? Continue aprendendo e se inspirando!
