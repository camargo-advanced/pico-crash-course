## Capítulo 11: Projeto Código Morse com um LED

Vamos viajar no tempo e descobrir a fascinante história por trás do Código Morse. Antes dos telefones e mensagens de texto, as pessoas precisavam de uma maneira especial de se comunicar à distância. E é aí que entra o Código Morse.

No início do século 19, um inventor chamado Samuel Morse queria encontrar uma maneira de enviar mensagens de longa distância usando eletricidade. Ele percebeu que podia representar letras e números usando uma combinação de pontos e traços. Cada letra e número no alfabeto recebeu sua própria sequência única de pontos '.' e traços '-'. Por exemplo, a letra 'A' foi representada como '**.-**' e o número '1' como '**.----**'. É como se cada letra e número tivesse seu próprio código secreto!

O Código Morse foi uma verdadeira revolução. Pela primeira vez na história, as pessoas podiam enviar mensagens através de fios telegráficos. Era como a Internet da época, mas sem computadores. Para enviar uma mensagem em Código Morse, você precisava de um dispositivo chamado telegrafo. Ao pressionar uma alavanca, você criava pontos e traços que eram transmitidos pelo fio até o destinatário.

Sabia que o famoso sinal de socorro SOS é simplesmente três pontos, três traços e mais três pontos? Isso se tornou um pedido universal de ajuda em situações de emergência!

O Código Morse pode ser representado também por luz. Esta é uma forma muito interessante de transmitir mensagens em situações onde a audição não é eficaz, como em ambientes ruidosos ou para pessoas com deficiência auditiva. 

Esta forma de comunicação por luz também é muito utilizada em situações de emergência, especialmente em ambientes escuros, como em operações de busca e resgate. Equipes de resgate podem usar lanternas para enviar mensagens em Código Morse para se comunicar em locais onde o som não seria ouvido.

Antigamente, e ainda em alguns casos hoje, a comunicação por luz em Código Morse é utilizada em operações militares e na navegação marítima. Luzes de sinalização específicas, como as lanternas de Aldis, eram usadas para enviar mensagens entre navios ou entre tropas no campo de batalha.

Para representar o Código Morse com luz, utilizamos dois estados: luz acesa por um curto período de tempo para representar o ponto '.' e a luz acesa por um período de tempo maior para representar o traço '-'.

A prática de transmitir mensagens em Código Morse com luz é uma habilidade valiosa e é frequentemente ensinada em treinamentos de escoteiros e em cursos de sobrevivência.

Que tal fazer um programa em MicroPython para transformar uma frase de texto em código morse e depois transmitir através de luz emitida por um LED? Faremos isso a seguir !

Antes vamos estudar um novo conceito em MicroPython chamado Dicionários. Precisaremos dele nesse projeto.

### Dicionários: Encontrando o Significado das Palavras

Um Dicionário é uma uma ferramenta incrível em MicroPython. É como ter um livro de referência onde podemos procurar o significado das palavras.

Imagine que você tem um dicionário de verdade. Nele, cada palavra tem um significado associado. Por exemplo, se procurarmos a palavra 'Girafa', encontramos a explicação sobre esse animal incrível. Nos dicionários em Python, as palavras são as chaves e os significados são os valores. Logo, dicionários armazenam pares com chave e valor.

Podemos criar um dicionário em MicroPython assim:

```python
dictionary = {'MicroPython': 'A powerful programming language', 'Cake': 'A delicious dessert'}
```

Aqui, 'MicroPython' e 'Cake' são as palavras (chaves) e as explicações são os significados (valores).

Se quisermos saber o que significa 'MicroPython', basta pedir assim:

```python
print(dictionary['MicroPython'])
```

E o retorno será 'A powerful programming language'! É como consultar um dicionário de verdade.

Se um dia decidirmos que queremos uma definição diferente para 'MicroPython', podemos atualizá-la assim:

```python
dictionary['MicroPython'] = 'A non-venomous snake found in some regions of the world'
```

Agora, a palavra 'MicroPython' terá um novo significado!

Dicionários são como nossos assistentes pessoais de referência. Eles nos ajudam a organizar informações e a encontrá-las rapidamente quando precisamos! 

Utilizaremos um dicionário para armazenar o código morse para cada letra do alfabeto em nosso projeto!

### Implementando o projeto 

O circuito para esse projeto é simples. Conecte um LED à porta **GP15** do Raspberry Pi Pico. Não esqueça de colocar um resistor entre o pino e o **GND**. Confirme a posição do pino **GND** no diagrama de layout do Pico. Uma forma de montar esse circuito é apresentada na figura a seguir.

![Imagem de circuito com 1 LED](/images/morse-circuit.png "Imagem de circuito com 1 LED")

Você também pode utilizar o LED embarcado **GP25** do Raspberry Pi Pico caso não deseje conectar componentes físicos externos. Nesse caso não esqueça de substituir o pino do LED do código para **25** (GP25).

Adicione este código a um novo arquivo no Thonny, salve-o em seu Raspberry Pi Pico como `morse.py` e depois execute-o. 

Para ver este circuito em funcionamento no simulador Wokwi, clique [aqui](https://wokwi.com/projects/382821932567843841).

```python
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
```

Programa 11.1

Experimente trocar o texto na 'Hello World' Por qualquer outra palavra ou frase e veja a sua representação luminosa em código morse no LED. Veja também que a conversão do texto original para a representação em pontos e traços do código morse é apresentada no Shell. Dessa forma você pode ver o código que será transmitido para luz.

Vamos desvendar esse código linha por linha.

```python
from machine import Pin, Timer
from time import sleep_ms
```
Essas são importações de bibliotecas. Elas trazem funcionalidades prontas para serem usadas no programa. A primeira linha traz comandos para controlar o hardware da placa. A segunda linha traz comandos relacionados ao tempo, como fazer o programa esperar por um tempo determinado.

```python
led = Pin(15, Pin.OUT)
```
Esta linha está configurando o pino `GP15` como um pino de saída `OUT` para controlar o LED. 

```python
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
     '9': '----.', '0': '-----'
}
```

Aqui nós criamos um dicionário chamado `morse_code`. Ele associa letras e números ao código Morse correspondente. Por exemplo, a letra 'A' é representada como '.-'.

```python
def flash_morse_code(morse):
    for char in morse:
        if char == '.':
            led.on()
            sleep_ms(200)
        elif char == '-':
            led.on()
            sleep_ms(600)
        led.off()
        sleep_ms(200)
```

Esta parte do código define uma função chamada `flash_morse_code`. Esta função faz o LED piscar para representar o código Morse. Se o caractere é um ponto '.', o LED pisca rapidamente. Se for um traço '-', o LED pisca por mais tempo.

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

Aqui temos outra função chamada `text_to_morse`. Ela transforma um texto em código Morse. Ela percorre cada caractere do texto e procura no dicionário `morse_code` para encontrar a representação em código Morse.

```python
code = text_to_morse("Hello World")
print("Morse Code:", code)
```

Esta parte converte a frase 'Hello World' em código Morse usando a função que acabamos de explicar. Em seguida, imprime o código Morse no Shell do Thonny.

```python
flash_morse_code(code)
```

Aqui, a função `flash_morse_code` é usada para fazer o LED piscar conforme o código Morse que acabamos de criar.

### Exercícios

#### Exercício 11.1: Mensagem Personalizada

Modifique o código fornecido para que ele transmita uma mensagem diferente em Código Morse. Substitua a linha code = text_to_morse("Hello World") por code = text_to_morse("SOS") para representar a mensagem "SOS". Execute o código e veja como a mensagem é transmitida através dos flashes do LED e dos sons do buzzer.

#### Exercício 11.2: Piscar um LED com Código Morse

Altere o código fornecido, acrescente o caractere "@" ao dicionário `morse_code` e defina a sequência de código morse como "... --- ...". Utilize a função `flash_morse_code` para fazer o LED piscar de acordo com a sequência de código morse definida. Execute o programa e observe o LED piscando de acordo com o código morse predefinido.

### Conclusão

Neste capítulo, exploramos o Código Morse, um sistema revolucionário de comunicação desenvolvido por Samuel Morse no século 19. Ele usou pontos e traços para representar letras, números e símbolos, permitindo mensagens à distância através de fios telegráficos.

O Código Morse não apenas facilitou a comunicação, mas também encontrou uso em situações onde a audição é ineficaz, como ambientes ruidosos ou para pessoas com deficiência auditiva. Sua utilização é comum em busca e resgate, navegação marítima e contextos militares.

Apresentamos os dicionários em MicroPython, ferramentas poderosas que associam chaves a valores. Mostramos como podemos usar um dicionário para mapear letras e números ao Código Morse.

Demonstramos um projeto prático em MicroPython que converte um texto em Código Morse e usa um LED para representar esse código por meio de flashes luminosos. Esta experiência prática possibilita visualizar a linguagem de comunicação por luz.

A jornada de aprendizado continua! Cada projeto é uma oportunidade para aprender e descobrir mais sobre eletrônica e programação. Parabéns pelo progresso até aqui! Continuem explorando e experimentando novas ideias!
