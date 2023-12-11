## Capítulo 7: Projeto Acionar um LED com um botão

Neste capítulo, mergulharemos na emocionante jornada de controle de um LED usando um botão com o Raspberry Pi Pico. Aqui, exploraremos os princípios básicos de eletricidade e circuitos, transformando-os em ações práticas por meio do MicroPython.

Preparem-se para aprender a conectar componentes, entender linhas de código e observar a mágica acontecer: um LED brilhando cada vez que o botão é pressionado. Com a orientação passo a passo e explicações detalhadas, estamos prontos para embarcar nessa aventura eletrizante!

Vamos controlar o LED usando um botão. Adicione um botão ao seu circuito conforme mostrado no diagrama abaixo. Note que você precisará de 5 fios de conexão, além de um botão, um resistor e um LED.

![LED e botão em uma placa de prototipagem](/images/button-and-led.png "LED e botão em uma placa de prototipagem")

Uma das extremidades do botão está conectada ao pino `GP14` do seu Raspberry Pi Pico e a outra extremidade do botão está conectada ao pino 3.3V. Ao configurar o pino do seu Pico, você precisa informar ao MicroPython que ele é um pino de entrada e precisa ser puxado para o nível lógico baixo (pull-down em inglês), o que significa que o pino lerá o valor lógico 0 (zero) caso o botão não esteja pressionado, e o valor lógico 1 (um) caso o botão esteja pressionado. Existem palavras-chave em MicroPython para esses valores lógicos: `True` é o mesmo que `1` e `False` é o mesmo que `0`.

Crie um novo arquivo, adicione o código a seguir e salve-o com o nome de `blink-pb.py` no seu Raspberry Pi Pico.

Para ver este circuito em funcionamento no simulador Wokwi, clique [aqui](https://wokwi.com/projects/382839490132061185).

```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        led.toggle()
        time.sleep(0.5)
```

Programa 7.1

Ao executar o código e ele fará com que o LED pisque cada vez que o botão é pressionado. Se o botão for mantido pressionado, o LED continuará piscando a cada meio segundo até que o botão seja solto.

Veja a seguir uma explicação de cada linha de código desse programa.

- `from machine import Pin`: importa uma biblioteca que permite ao Raspberry Pi Pico controlar os seus pinos. Por exemplo, podemos alternar a tensão de um pino entre alta (3,3 V) e baixa (0 V).

- `import time`: importa a biblioteca que permite lidar com o temporizadores. Com isso podemos fazer o programa esperar por um tempo específico sem fazer nada por exemplo.

- `led = Pin(15, Pin.OUT)`: cria uma variável chamada `led` (que poderia ser qualquer outro nome) dizendo que ela está conectada ao pino 15 (`GP15`) do seu Raspberry Pi Pico. Além disso, está configurando este pino como uma saída `Pin.OUT`. Isso significa que esse pino pode enviar corrente elétrica para acender um LED conectado a ele através de um fio de conexão.

- `button = Pin(14, Pin.IN, Pin.PULL_DOWN)`: cria uma variável chamada `button` conectada ao pino 14 (`GP14`) do seu Raspberry Pi Pico. O pino é configurando como uma entrada `Pin.IN`. Isso significa que o pino pode 'escutar' se existe eletricidade passando por ele ou não. O `Pin.PULL_DOWN` significa que há um resistor interno especial ligado ao pino que ajuda a manter o valor do pino como 0 V quando não há corrente elétrica.

- `while True:`: inicia um 'loop' que vai continuar para sempre, a menos que algo o pare. É como dizer: repita isso para sempre.

A palavra-chave `while` ('enquanto' em Português) permite que um pedaço de código seja repetido várias vezes, enquanto a condição fornecida seja verdadeira. O `while` funciona assim: primeiro, verifica se uma condição é verdadeira. Se for, ele executa o bloco de código dentro dele. Depois, ele verifica a condição novamente. Se ainda for verdadeira, ele executa o bloco de código novamente. Isso se repete até que a condição não seja mais verdadeira. Quando isso acontece, o programa continua a partir da linha de código após o `while`. Como em nosso caso a condição avaliada é a palavra-chave `True`, o loop se repetirá para sempre.

- `if button.value():` verifica se o botão está sendo pressionado. A palavra chave `if` executa o bloco de código indentado caso a condição lógica fornecida `button.value()` seja avaliada como verdadeira, ou `True`. Caso contrário o bloco indentado não será executado. `button.value()` retorna `True` se o botão estiver pressionado e `False` se o botão estiver solto. 

A palavra-chave `if` ('se' em Português) permite ao programa tomar decisões com base em certas condições. É como quando você tem que decidir algo na vida real: 'Se' estiver chovendo, então leve um guarda-chuva. Ao usar o `if` em programação, você está dando uma ordem para MicroPython verificar se algo é verdadeiro ou falso. Dependendo do resultado dessa verificação, o programa irá seguir um caminho ou outro. 

- `led.toggle()`: muda o estado do LED. Se o LED estiver aceso, ele é apagado, e vice-versa. Note que essa linha de código está dentro da condição `if`. Logo, somente quando o botão estiver sendo pressionado essa linha será executada.

- `time.sleep(0.5)`: faz o programa esperar por meio segundo (0,5 segundos) antes de continuar. É como um pequeno intervalo de tempo para que possamos ver o LED piscar. Note que essa linha de código também está dentro da condição `if`. Logo, somente quando o botão estiver sendo pressionado essa linha será executada.

### Exercícios

#### Exercício 7.1: Piscando o LED com pausas diferentes

Desafie-se a modificar o código para que o LED pisque em intervalos de tempo diferentes. Tente fazer com que o LED pisque duas vezes mais rápido alterando os tempos de pausa no código. Depois, faça com que o LED pisque duas vezes mais devagar alterando os tempos de pausa no código.

#### Exercício 7.2: Botão para acender e apagar o LED

Modifique o código para que o LED permaneça aceso enquanto o botão estiver pressionado e se apague quando o botão for solto. Esta mudança requer alterações na lógica do código para controlar o estado do LED com base na leitura contínua do botão.

#### Exercício 7.3: Botão Invertido

Altere a lógica do botão para funcionar invertido. Ou seja, o LED deve piscar quando o botão não estiver pressionado e permanecer aceso quando pressionado.

#### Exercício 7.4: Piscar LEDs alternadamente

Adicione um segundo LED ao circuito e altere o código para fazer com que os LEDs pisquem alternadamente quando o botão for pressionado.

#### Exercício 7.5: Botão de Desligamento

Modifique o código para usar o botão como um interruptor. Pressionar o botão liga o LED e mantém aceso até que o botão seja pressionado novamente para desligá-lo.

### Conclusão

E assim, concluímos mais um capítulo repleto de descobertas fascinantes no mundo da eletrônica e programação. Ao controlar um LED com um botão, mergulhamos nas nuances da programação em MicroPython e na interação de componentes eletrônicos, transformando conceitos teóricos em experiências tangíveis.

Ao compreender e executar o código fornecido, vimos o LED responder aos comandos do botão, piscando a cada pressionamento. Aprendemos sobre a configuração dos pinos, o uso de estruturas condicionais e a importância dos loops no funcionamento do programa.

Este capítulo representa apenas o começo de uma jornada emocionante e repleta de possibilidades. Com a base estabelecida, estamos prontos para explorar ainda mais, construindo projetos mais complexos e desafiadores. Com determinação e curiosidade, continuaremos a desbravar este vasto universo da eletrônica e da programação, transformando ideias em realidade de forma criativa e inovadora.
