## Capítulo 13: Projeto Tocando músicas com um Buzzer

Você sabia que é possível criar melodias e sons incríveis usando apenas um Raspberry Pi Pico e um pequeno componente chamado buzzer? Neste capítulo, vamos explorar o emocionante universo da música com buzzer, e você aprenderá como fazer isso de uma forma simples e divertida.

Relembre que um buzzer é um dispositivo eletrônico que pode emitir sons quando uma corrente elétrica é aplicada a ele. É como um pequeno alto-falante que produz tons simples, permitindo-nos criar melodias divertidas e efeitos sonoros interessantes.

Assim como em uma linguagem, onde temos letras que formam palavras, na música, temos as 'notas' que se combinam para criar melodias emocionantes. Cada nota tem um nome, como Dó, Ré, Mi, e assim por diante, e essas notas têm frequências específicas que determinam o som que ouvimos.

A frequência de uma nota determina se ela soa grave ou aguda. Notas com frequências mais baixas, como o Dó, soam mais graves, enquanto notas com frequências mais altas, como o Sol, soam mais agudas.

Assim como em uma música que você escuta no rádio, a música que criaremos terá um ritmo. O ritmo é a pulsação da música e nos diz quando uma nota começa e termina.

### Notas musicais 

Em nosso código utilizaremos 88 notas musicais que correspondem à notação musical ocidental e são todas as notas que você pode encontrar em um teclado de tamanho padrão.

![Imagem de teclado padrão ocidental](/images/keyboard.png "Imagem de teclado padrão ocidental")

Segue a lista completa de notas musicais que utilizaremos:

`b0` `c1` `c#1` `d1` `d#1` `e1` `f1` `f#1` `g1` `g#1` `a1` `a#1` `b1` `c2` `c#2` `d2` `d#2` `e2` `f2` `f#2` `g2` `g#2` `a2` `a#2` `b2` `c3` `c#3` `d3` `d#3` `e3` `f3` `f#3` `g3` `g#3` `a3` `a#3` `b3` `c4` `c#4` `d4` `d#4` `e4` `f4` `f#4` `g4` `g#4` `a4` `a#4` `b4` `c5` `c#5` `d5` `d#5` `e5` `f5` `f#5` `g5` `g#5` `a5` `a#5` `b5` `c6` `c#6` `d6` `d#6` `e6` `f6` `f#6` `g6` `g#6` `a6` `a#6` `b6` `c7` `c#7` `d7` `d#7` `e7` `f7` `f#7` `g7` `g#7` `a7` `a#7` `b7` `c8` `c#8` `d8` `d#8`

### Transformando partituras em notas

Você pode inserir notas musicais reais e criar melodias para tocar no seu buzzer.

Uma letra é usada para representar a nota musical e um número é usado para indicar onde a nota aparece na clave de sol.

![Uma partitura com um Dó central colocado na clave de sol](/images/middle-c.png "Uma partitura com um Dó central colocado na clave de sol")

Por exemplo, o Dó central está no centro da clave de sol e usa c4.

Quando você sobe na clave de sol, o número aumenta. Quando você desce na clave de sol, o número diminui.

![Uma partitura mostrando as notas subindo e descendo na pauta](/images/cdef-cdef.png "Uma partitura mostrando as notas subindo e descendo na pauta")

Sua partitura musical pode incluir notas que são sustenidos. Estes são representados usando o símbolo #. No exemplo abaixo, a primeira nota é um Dó sustenido. Um Dó sustenido é c#4.

![Uma partitura musical mostrando notas que são sustenidos](/images/sharp-notes.png "Uma partitura musical mostrando notas que são sustenidos")

Sua partitura musical pode incluir notas que são bemóis. Estes também serão representados usando um # porque não temos bemóis em nossa lista de notas. Para transformar um bemól em um sustenido, você precisa descer na escala.

- Um Ré bemol se torna um Dó sustenido ou c#4
- Um Mi bemol se torna um Ré sustenido ou d#4
- Um Sol bemol se torna um Fá sustenido ou f#4
- Um Lá bemol se torna um Sol sustenido ou g#4

![Uma partitura musical mostrando notas que são bemóis](/images/flat-notes.png "Uma partitura musical mostrando notas que são bemóis")

Usaremos um Raspberry Pi Pico e um pouco de código em MicroPython para dizer ao buzzer quando tocar cada nota e por quanto tempo. Isso nos permite criar músicas incríveis com apenas algumas linhas de código!

Vamos Começar!

### Escrevendo o programa

Vamos implementar a música Brilha, Brilha, Estrelinha (Twinkle, Twinkle, Little Star em inglês). 

Não será necessário fazer nenhuma alteração no circuito que você já possui. Neste exemplo, você usará o buzzer e o LED.

Adicione este código a um novo arquivo no Thonny, salve-o em seu Raspberry Pi Pico como `song.py` e depois execute-o. 

Para ver este circuito em funcionamento no simulador Wokwi, clique [aqui](https://wokwi.com/projects/382846451199811585).

```python
from machine import Pin, PWM
from utime import sleep_ms

# Configurando o pino 15 como saída para controlar o LED
led = Pin(15, Pin.OUT)

# Configurando o buzzer 
buzzer = PWM(Pin(16))
buzzer.duty_u16(0)  # Desliga o buzzer inicialmente

# Definindo as notas e pausas com as respectivas durações
song = ["C4", "C4", "G4", "G4", "A4", "A4", "G4", "P",
        "F4", "F4", "E4", "E4", "D4", "D4", "C4", "P",
        "G4", "G4", "F4", "F4", "E4", "E4", "D4", "P",
        "G4", "G4", "F4", "F4", "E4", "E4", "D4", "P",
        "C4", "C4", "G4", "G4", "A4", "A4", "G4", "P",
        "F4", "F4", "E4", "E4", "D4", "D4", "C4"]

# Dicionário de frequências das notas
tones = {
    "B0": 31, "C1": 33, "C#1": 35, "D1": 37, "D#1": 39, "E1": 41, "F1": 44, 
    "F#1": 46, "G1": 49, "G#1": 52, "A1": 55, "A#1": 58, "B1": 62, "C2": 65,
    "C#2": 69, "D2": 73, "D#2": 78, "E2": 82, "F2": 87, "F#2": 93, "G2": 98,
    "G#2": 104, "A2": 110, "A#2": 117, "B2": 123, "C3": 131, "C#3": 139,
    "D3": 147, "D#3": 156, "E3": 165, "F3": 175, "F#3": 185, "G3": 196,
    "G#3": 208, "A3": 220, "A#3": 233, "B3": 247, "C4": 262, "C#4": 277,
    "D4": 294, "D#4": 311, "E4": 330, "F4": 349, "F#4": 370, "G4": 392,
    "G#4": 415, "A4": 440, "A#4": 466, "B4": 494, "C5": 523, "C#5": 554,
    "D5": 587, "D#5": 622, "E5": 659, "F5": 698, "F#5": 740, "G5": 784,
    "G#5": 831, "A5": 880, "A#5": 932, "B5": 988, "C6": 1047, "C#6": 1109,
    "D6": 1175, "D#6": 1245, "E6": 1319, "F6": 1397, "F#6": 1480, "G6": 1568,
    "G#6": 1661, "A6": 1760, "A#6": 1865, "B6": 1976, "C7": 2093, "C#7": 2217,
    "D7": 2349, "D#7": 2489, "E7": 2637, "F7": 2794, "F#7": 2960, "G7": 3136,
    "G#7": 3322, "A7": 3520, "A#7": 3729, "B7": 3951, "C8": 4186, "C#8": 4435,
    "D8": 4699, "D#8": 4978
}

# Função para tocar uma nota
def play_tone(note):
    if note in tones: 
        buzzer.freq(tones[note])
        buzzer.duty_u16(1000)
        led.on()
        sleep_ms(300)  
        buzzer.duty_u16(0)
        led.off() 
        sleep_ms(100)  
    else:
        sleep_ms(400)  

# Função para tocar a música
def play_song(song):
    for note in song:
        play_tone(note)

# Toca a música
play_song(song)
```

Programa 13.1

Vamos desvendar esse código passo-a-passo a seguir!

```python
from machine import Pin, PWM
from utime import sleep_ms
```
Aqui estamos importando algumas bibliotecas necessárias. A biblioteca `machine` permite o controle de pinos do microcontrolador e a biblioteca `utime` é usada para gerar pausas em milissegundos.

```python
led = Pin(15, Pin.OUT)
buzzer = PWM(Pin(16))
buzzer.duty_u16(0)
```

Aqui estamos configurando dois componentes: um LED no pino `15` (GP15) e um buzzer no pino `16` (GP16). O LED é configurado como saída (`Pin.OUT`) para que possa ser controlado para acender ou apagar. O buzzer é configurado usando `PWM` (Modulação por Largura de Pulso), o que permite controlar a frequência e o tempo de atividade do sinal, permitindo assim criar diferentes tons.

```python
song = ["C4", "C4", "G4", "G4", "A4", "A4", "G4", "P",
        "F4", "F4", "E4", "E4", "D4", "D4", "C4", "P",
        "G4", "G4", "F4", "F4", "E4", "E4", "D4", "P",
        "G4", "G4", "F4", "F4", "E4", "E4", "D4", "P",
        "C4", "C4", "G4", "G4", "A4", "A4", "G4", "P",
        "F4", "F4", "E4", "E4", "D4", "D4", "C4"]
```

Aqui definimos uma lista chamada `song` que contém uma série de notas musicais (C4, G4, etc.) e P representa uma pausa. Essa lista forma a música que será tocada. Nesse caso trata-se da música Brilha, Brilha, Estrelinha.

```python
tones = {
    "B0": 31, "C1": 33, "C#1": 35, "D1": 37, "D#1": 39, "E1": 41, "F1": 44, 
    "F#1": 46, "G1": 49, "G#1": 52, "A1": 55, "A#1": 58, "B1": 62, "C2": 65,
    # ...
    # Muitas frequências associadas a notas musicais
    # ...
    "D8": 4699, "DS8": 4978
    }
```

Aqui criamos um dicionário chamado `tones` que associa notas musicais com suas respectivas frequências em hertz.

```python
def play_tone(note):
    if note in tones: 
        buzzer.freq(tones[note])
        buzzer.duty_u16(1000)
        led.on()
        sleep_ms(300)  
        buzzer.duty_u16(0)
        led.off() 
        sleep_ms(100)  
    else:
        sleep_ms(400)  
```

A função `play_tone` toca uma única nota. Primeiro, verifica se a nota está no dicionário `tones`. Se estiver, configura a frequência do buzzer e o aciona. Em seguida, acende o LED. Após um curto período, desliga o buzzer e apaga o LED.

Se a nota não for encontrada no dicionário, isso significa que é uma pausa, então a função apenas espera por um tempo antes de prosseguir.

```python
def play_song(song):
    for note in song:
        play_tone(note)
```

Esta função `play_song` percorre a lista `song` e chama a função `play_tone` para tocar cada nota ou pausa.

```python
play_song(song)
```

Finalmente, esta linha de código chama a função `play_song` para tocar a música definida na lista `song`.

### Tocando outras músicas

Agora que já implementou e ouviu a música Brilha, Brilha, Estrelinha, que tal ouvir outras músicas?

**Happy Birthday**:

```python
song = [
    "C4", "C4", "D4", "C4", "F4", "E4", "P",
    "C4", "C4", "D4", "C4", "G4", "F4", "P",
    "C4", "C4", "C5", "A4", "F4", "E4", "D4", "P",
    "A#3", "A#3", "A3", "F4", "G4", "F4"
]
```

**Jingle Bells**:

```python
song = [
    "E4", "E4", "E4", "P", "E4", "E4", "E4", "P", 
    "E4", "G4", "C4", "D4", "E4", "P",
    "F4", "F4", "F4", "F4", "F4", "E4", "E4", "E4", 
    "E4", "D4", "D4", "E4", "D4", "P",
    "E4", "E4", "E4", "E4", "E4", "E4", "P", "E4", 
    "G4", "C4", "D4", "E4", "P",
    "F4", "F4", "F4", "P", "F4", "E4", "E4", "P",
    "G4", "G4", "F4", "D4", "C4"
]
```

**Ode to Joy** (Hino à Alegria de Beethoven):

```python
song = [
    "E4", "E4", "F4", "G4", "G4", "F4", "E4", 
    "D4", "C4", "C4", "D4", "E4", "E4", "D4", "D4", "P",
    "E4", "E4", "F4", "G4", "G4", "F4", "E4", 
    "D4", "C4", "C4", "D4", "E4", "D4", "C4", "C4"
]
```

Você pode substituir a variável `song` por qualquer uma dessas listas de notas para tocar a música correspondente. 

### Exercícios

#### Exercício 13.1: Alteração de Notas

Experimente alterar a melodia no código fornecido para tocar uma música diferente, como "Happy Birthday", "Jingle Bells" ou qualquer outra melodia conhecida. Substitua a lista `song` por uma nova sequência de notas da música desejada, seguindo o padrão de notas e pausas utilizado no exemplo.

#### Exercício 13.2: Criar uma Melodia

Desafie-se a criar sua própria melodia! Escolha uma sequência de notas musicais para formar uma melodia simples e substitua a lista `song` no código original pela sua sequência de notas personalizada. Execute o código no Raspberry Pi Pico para ouvir sua composição musical reproduzida pelo buzzer.

#### Exercício 13.3: Ritmo Personalizado

Altere a duração de algumas notas na sequência para criar um ritmo diferente. Experimente modificar o tempo de algumas notas (alterando os valores de pausa) para variar o ritmo da melodia e dar-lhe uma sensação única.

### Conclusão

Nesse capítulo você explorou o mundo emocionante da criação musical. O buzzer é um dispositivo que, quando conectado ao Raspberry Pi Pico, pode produzir melodias e efeitos sonoros fascinantes.

Assim como na linguagem escrita, onde as letras formam palavras, na música, as notas se unem para criar melodias cativantes. Cada nota possui um nome, como Dó, Ré, Mi, entre outros, e possui frequências específicas que determinam o som que ouvimos. A variação na frequência das notas também determina se elas soam graves ou agudas.

Exploramos um conjunto de 88 notas musicais, correspondentes à notação musical ocidental, que podem ser utilizadas para criar suas próprias melodias. Você aprendeu a representar essas notas usando uma letra associada a um número na clave de sol.

Com o auxílio do Raspberry Pi Pico e um código em MicroPython, conseguimos dizer ao buzzer quando tocar cada nota e por quanto tempo. Isso nos permitiu criar músicas incríveis com apenas algumas linhas de código!

Ao implementar o exemplo da música "Brilha, Brilha, Estrelinha", você já deu um passo significativo. Além disso, sugerimos outras músicas como "Happy Birthday", "Jingle Bells" e "Ode to Joy", proporcionando uma oportunidade para expandir seu conhecimento e diversificar as melodias que pode reproduzir.

Agora você está pronto para experimentar e explorar a criação de suas próprias músicas usando o Raspberry Pi Pico e o buzzer. Através da combinação de diferentes notas e ritmos, você pode dar vida a composições musicais incríveis. Estamos ansiosos para ver as músicas surpreendentes que você será capaz de criar!
