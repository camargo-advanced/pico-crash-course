## Projeto: Batalha dos Botões

Este é um emocionante desafio de agilidade projetado especialmente para dois jogadores que estão prontos para testar seus reflexos e habilidades de reação!

Neste jogo, vocês serão desafiados a pressionar um botão no momento exato em que a luz se apagar. Parece simples, certo? No entanto, a velocidade é essencial, e qualquer hesitação pode custar a vitória! 

Mas tome cuidado, se algum jogador pressionar o botão antes da luz se apagar, perde o jogo!

Ao longo deste capítulo, vamos guiar você através do código que faz tudo acontecer. Vocês vão aprender como configurar os botões, controlar a luz e calcular o tempo de reação. 

Então, preparem-se para uma competição emocionante e descubram quem entre vocês será coroado como o campeão da Batalha dos Botões. Vamos lá!

### Interrupções 

Em MicroPython uma interrupção (Interrupt em inglês) é um mecanismo que permite que um programa pare temporariamente sua execução para lidar com um evento externo. No contexto de hardware, isso geralmente significa responder a um sinal elétrico gerado por um componente, como um botão pressionado.

A utilização de interrupções é especialmente útil para lidar com eventos em tempo real, como um botão pressionado, sem a necessidade de ficar constantemente verificando o estado do botão em um loop. Em vez disso, o programa pode continuar sua execução normal até que uma interrupção seja acionada.

Aqui está um exemplo de como usar uma interrupção para tratar um botão pressionado em MicroPython:

```python
from machine import Pin

# Configuração do botão
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Function to handle the interrupt
def button_pressed(b):
    button.irq(handler=None) 
    print("Button pressed!")

# Set up the interrupt on the button
button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)

# The program continues to run normally
while True:
    pass

```

Neste exemplo a função `button_pressed` será chamada quando o botão for pressionado. `trigger=Pin.IRQ_RISING` indica que queremos que a função `button_pressed` seja chamada quando o botão fizer a transição de estado de nível de tensão baixo (Low) para nível de tensão alto (High), ou seja, quando for pressionado.

Enquanto o programa está no loop `while True`, ele continua executando normalmente, mas mas pode ser interrompido a qualquer momento quando o botão for pressionado.

### Efeito bounce

Imagine que você tem um botão em um videogame. Quando você pressiona o botão, quer que algo aconteça, certo? Por exemplo, em um jogo de corrida, você quer que o carro acelere quando você aperta o botão de aceleração.

Agora, às vezes, o botão pode ficar um pouco agitado. Isso significa que, quando você pressiona o botão, ele pode fazer uma coisa tipo: pressionar, soltar, pressionar novamente bem rápido. É como se o botão piscasse rapidamente. Para o computador, ele pode entender isso como várias pressões de botão em vez de apenas uma. Esse efeito indesejado chama-se bounce.

O debounce é como uma ajuda que colocamos para evitar o efeito bounce. Ele verifica se o botão foi realmente pressionado, e não se está apenas piscando. Imagina que é como se alguém estivesse olhando atentamente para o botão e dizendo: Ok, isso foi uma pressão de verdade!

Adicionar a linha `button.irq(handler=None)` no exemplo anterior desativa a interrupção no pino do botão. Isso significa que, uma vez que o botão foi pressionado e a interrupção foi ativada, o programa não irá mais responder a novas interrupções provenientes desse botão até que a interrupção seja explicitamente reativada.

Experimente rodar o programa acima com um botão de acordo com o circuito do Programa 5. Note que ao pressionar o botão apenas uma mensagem aparece no Shell do Thonny. 

Agora remova a linha `button.irq(handler=None)` e rode novamente o programa. Note que agora várias mensagens aparecem no Shell. Isso ocorre por causa do efeito de bounce dos botões que levam um tempo para estabilizar os contatos elétricos e com isso geram esse efeito indesejado de piscar que é entendido pela porta do RaspBerry Pi Pico como se o botão tivesse sido pressionado várias vezes. 

### Montando o circuito

Primeiramente monte o circuito do jogo colocando um led vermelho no pino GP15 do seu Raspberry Pi Pico. Lembre de colocar um resistor para limitar a corrente conforme discutido em exemplos anteriores, como por exemplo, um resistor de 220 Ohms.

Coloque também dois botões no circuito para que sejam utilizados pelos jogadores. Um dos botões deve ser colocando no pino GP16 e o outro no pino GP17 do seu Raspberry Pi Pico.

Uma forma de montar esse circuito segue na figura que segue. Agora que você já entende um pouco mais de desenho de circuitos, sabe que existem várias outras possíveis maneiras de montar esse circuito. Fique a vontade para fazer de acordo com o que for mais interessante para você!

![Circuito do jogo da reação](/images/reaction-circuit.png "Circuito do jogo da reação")

### Codificando o jogo

É hora de você colocar a mão na massa e criar esse jogo!  Adicione este código a um novo arquivo no Thonny, salve-o em seu Raspberry Pi Pico como `reaction.py` e depois execute-o. 

Para ver este circuito em funcionamento no simulador Wokwi, clique [aqui](https://wokwi.com/projects/382823962591290369).

```python
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
```

Programa 13.

Agora vamos desvendar como tudo funciona.

```python
from machine import Pin
from time import sleep_ms, ticks_ms, ticks_diff
from random import randint
```

Esta parte do código está importando algumas ferramentas que vamos usar no jogo. Coisas como controlar os pinos como botões e luzes, medir o tempo e gerar números aleatórios.

```python
# Configuração dos pinos
led = Pin(15, Pin.OUT)
right_button = Pin(16, Pin.IN, Pin.PULL_DOWN)
left_button = Pin(17, Pin.IN, Pin.PULL_DOWN)
```

Aqui, estamos configurando os pinos do nosso equipamento. O pino **GP15** é para o led, e os pinos **GP16** e **GP17** são para os botões, um para o jogador da direita e outro para o jogador da esquerda.

```python
pressed_button = None
```

Criamos uma variável chamada `pressed_button` para guardar informações sobre qual botão foi pressionado. No começo, não sabemos qual botão foi pressionado, então deixamos como `None` que significa Nada.

```python
def button_pressed(pin):
    right_button.irq(handler=None)
    left_button.irq(handler=None)
    global pressed_button
    pressed_button = pin
```

A função `button_pressed` é chamada quando um botão for pressionado. Ela diz que o botão direito `right_button` não deve mais chamar essa função quando pressionado novamente. O mesmo é feito para o botão esquerdo. Isso é uma estratégia para evitar o efeito indesejado da flutuação dos contatos elétricos do botão, ou seja, o bounce. Depois, ela guarda qual botão foi pressionado na variável `pressed_button`. 

Note que utilizamos uma variável global. Variáveis globais são declaradas geralmente no início do programa e para serem acessadas e sofrer alterações dentro de uma função, precisam ser declaradas como globais no contexto da função. Isso é feito na linha `global pressed_button`. Feito isso, pode-se acessar ou alterar o valor da variável global. Nesse caso estamos atribuindo o valor do botão pressionado à variável global pois precisaremos dessa informação posteriormente.

```python
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
```

A função `pressed_in_waiting` é usada para simular o tempo de espera antes do jogo começar, quando os jogadores precisam esperar antes de pressionar o botão.

`waiting_time = randint(1, 5) * 1000` define um tempo de espera aleatório entre 1 e 5 segundos. O número é multiplicado por 1000 para converter segundos em milissegundos.

A linha `led.high()` acende a luz para sinalizar aos jogadores que eles precisam se preparar para o jogo começar.

Na linha `timer_start = ticks_ms()`, estamos marcando o momento exato em que a espera começa. Vamos usar isso para medir quanto tempo se passou caso o jogador pressione o botão durante o tempo de espera.

A linha  `while ticks_diff(ticks_ms(), timer_start) < waiting_time:` começa um loop que vai continuar até o tempo de espera acabar. O `ticks_diff` nos diz quanto tempo se passou desde que a espera começou.

Em `if pressed_button is not None: break` estamos verificando se um jogador pressionou um botão durante a espera. Se isso acontecer, vamos sair do loop.

Depois que o tempo de espera acabar, a declaração `if / elif` verifica qual jogador pressionou o botão. Se foi o jogador da esquerda, dizemos que o jogador da esquerda perdeu. Se foi o jogador da direita, dizemos que o jogador da direita perdeu.

Em `led.low()` apagamos a luz para indicar que a espera acabou.

Ao final a função `pressed_in_waiting` retorna qual botão foi pressionado durante a espera. No cenário ideal, a função retornará `None` indicando que nenhum jogador pressionou o botão durante o período de espera, dado que o jogador só deve pressionar o botão após a luz se apagar.

```python
def main_game():
    left_button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)
    right_button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)

    if pressed_in_waiting() is None:
        timer_start = ticks_ms()

        while pressed_button is None: 
            sleep_ms(5)
                
        if pressed_button is left_button:
            print("Left Player wins!")
        elif pressed_button is right_button:
            print("Right Player wins!")
            
        timer_reaction = ticks_diff(ticks_ms(), timer_start)
        print("Time to react: " + str(timer_reaction) + " milliseconds!")

main_game()
```

A função `main_game` é o coração do nosso jogo, onde toda a ação acontece.

Na linha `left_button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)` estamos configurando os botões para serem sensíveis a interrupções. Isso significa que quando um dos botões é pressionado, eles vão chamar a função `button_pressed`. Isso é feito para os dois botões: o que representa o jogador direito, e um para o jogador esquerdo.

Em `if pressed_in_waiting():  is None:` estamos verificando se nenhum botão foi pressionado durante a fase de espera. Se nenhum botão foi pressionado, significa que os jogadores estão prontos para jogar.

A linha `timer_start = ticks_ms()` marca o momento exato em que o jogo começa. Vamos usar isso para medir quanto tempo os jogadores levam para reagir.

O loop `while` continua até que um dos jogadores pressione um botão. Enquanto isso, o jogo fica "pausado" aqui.

Depois que um botão é pressionado, verificamos qual jogador ganhou na declação `if / elif`. Dependendo do botão pressionado, imprimimos na tela quem foi o vencedor.

Na sequência calculamos quanto tempo levou para o jogador reagir em `timer_reaction = ticks_diff(ticks_ms(), timer_start)`. Isso é mostrado na tela para que os jogadores possam ver o tempo de reação do jogador vencedor.

Agora que você entendeu como o jogo de reação funciona, chegou a hora de colocar suas habilidades à prova! Lembre-se, a prática leva à excelência, e cada vez que você joga, está dando um passo em direção à maestria.

Continue a explorar e aprender, pois o mundo da programação e da eletrônica reserva inúmeras aventuras emocionantes para você. Você está no caminho certo para se tornar um verdadeiro mestre no universo da tecnologia.
