## Projeto: Piscando um LED externo

### Descobrindo os Segredos da Eletricidade

Bem-vindo a um mundo emocionante onde a eletricidade se torna mágica! A eletricidade é uma forma de energia que pode ser controlada e utilizada para fazer coisas incríveis. Ela é composta por minúsculas partículas chamadas elétrons, que agem como mensageiros de energia.

Os elétrons percorrem caminhos invisíveis chamados circuitos. Imagine-os como estradas especiais, onde a energia viaja para alimentar nossos projetos. Em um circuito, a eletricidade sempre flui de um ponto de tensão alta para um ponto de tensão baixa.

Um LED é como uma pequena lâmpada que emite luz quando a eletricidade passa por ele. Quando escrevemos `pin.high()`, estamos dizendo ao Raspberry Pi Pico para configurar aquele pino com um nível de tensão alto, geralmente 3,3V, permitindo a passagem de corrente elétrica (elétrons) através do LED e retornando para o terra (GND, ground em inglês), que tem um nível de tensão de 0V.

> **`Atenção`**: Estudaremos LEDs em detalhes mais adiante nesse curso.

É fundamental garantir que o circuito esteja completamente conectado, com todos os componentes eletricamente unidos, para permitir o fluxo da corrente elétrica. É aqui que uma placa de prototipagem e fios de conexão podem ajudar, como veremos adiante.

Por outro lado, `pin.low()` faria o oposto, configurando o pino para ter um nível de tensão como baixo, ou 0V, o que efetivamente corta a energia no pino e não permite que a corrente elétrica flua. Lembre que os elétros somente fluem de um nível de tensão alto para um nível de tensão mais baixo. Como nesse caso o pino e o terra estão em nível de tensão baixo de 0V (ou seja mesma tensão), os elétros não fluem. 

### Usando uma Placa de Prototipagem

Uma placa de prototipagem está coberta com pequenos furos ou orifícios espaçados com 2,54 mm de distância. Debaixo desses orifícios, existem tiras de metal que funcionam como os fios de conexão, identificadas em verde na figura que segue. As tiras de metal percorrem em fileiras pela placa, com a maioria das placas tendo uma abertura no meio para dividi-las em dois lados.

![Placa de prototipagem](/images/breadboard-internal-wiring.png "Placa de prototipagem")

Muitas placas de prototipagem têm letras na parte superior e números nas laterais. Isso permite que você encontre um orifício específico: A1 é o canto superior esquerdo, B1 é o orifício imediatamente à direita, enquanto B2 é um orifício abaixo dali. A1 está conectado a B1 pelas tiras de metal ocultas, mas nenhum orifício marcado com um 1 está conectado a qualquer orifício marcado com um 2, a menos que você adicione um fio de conexão por conta própria. 

Placas de prototipagem maiores têm fileiras de orifícios nas laterais, geralmente marcadas com listras vermelhas e pretas ou vermelhas e azuis. Estas são as trilhas de energia e são projetadas para facilitar a conexão dos fios: por exemplo, você pode conectar um único pino **GND** do seu Pico a uma das trilhas de energia, que são normalmente marcadas com uma listra azul ou preta e um símbolo de menos, para fornecer um terra comum para muitos componentes na placa. Você pode fazer o mesmo se o seu circuito precisar de energia de 3,3V utilizando a trilha com listra vermelha. Todos os orifícios de uma mesma trilha estão conectados eletricamente. 

Inserir componentes eletrônicos a uma placa de prototipagem é simples: alinhe seus terminais (as partes metálicas salientes) com os orifícios e empurre suavemente até que o componente esteja no lugar. Nunca tente inserir mais de um terminal de componente ou fio de conexão em um mesmo orifício na placa. 

> **`Importante`**: Os orifícios estão conectados em fileiras, exceto pela divisão no meio, então o terminal de componente inserido em A1 está eletricamente conectado a qualquer coisa que você insira em B1, C1, D1 e E1, e não conectado aos orifícios F1, G1, H1, I1 ou J1. 

### Resistores

Os resistores são usados em circuitos para reduzir a corrente elétrica. Isso os torna úteis na proteção de certos componentes que podem ser danificados se uma corrente muito alta passar por eles. Também são úteis para garantir que uma corrente ou tensão específica seja fornecida a um componente, como por exemplo um LED.

![Array de Resistores Eletrônicos de Pinos Axiais](/images/resistors.jpg "Array de Resistores Eletrônicos de Pinos Axiais")

A resistência à passagem de corrente elétrica de um resistor é medido em Ohms e utiliza o símbolo Ω.

Você pode determinar o valor da resistência de um resistor pela cor das faixas nele presentes. A maioria dos resistores possui 4 faixas, mas resistores de 5 e 6 faixas também estão disponíveis.

Em um resistor de 4 faixas, a primeira cor indica o primeiro dígito do valor, a segunda faixa indica o segundo dígito do valor, e a terceira faixa indica o que multiplicar pelos dois primeiros dígitos ou quantos zeros adicionar no final. A quarta faixa indicará a precisão do valor do resistor calculada como uma porcentagem.

![Código de cores em resistores](/images/color-code-resistors.png "Código de cores em resistores")

Por exemplo, é possível calcular o valor em Ohms destes resistores da seguinte forma:

![Resistor mostrando faixas de vermelho, vermelho, marrom](/images/220-resistor.png "Resistor mostrando faixas de vermelho, vermelho, marrom")

Vermelho Vermelho Marrom = 2 2 x 10 = 220Ω.

![Resistor mostrando faixas de violeta, verde, preto](/images/75-resistor.png "Resistor mostrando faixas de violeta, verde, preto")

Violeta Verde Preto = 7 5 x 1 = 75Ω.

### LEDs

Um LED (Light Emitting Diode em inglês) é um componente eletrônico que emite luz quando uma corrente elétrica o atravessa. Ele é construído a partir de materiais que têm propriedades especiais para esse efeito. A cor da luz emitida pelo LED depende do tipo de material utilizado. Diferentes materiais resultam em cores variadas, como vermelho, verde, azul, entre outras.

![3 LEDs nas cores vermelho, verde e azul](/images/3-leds-rgb.jpg "3 LEDs nas cores vermelho, verde e azul")

Normalmente, é necessário usar um resistor com um LED. Isso ocorre porque uma corrente elétrica muito alta pode fazer com que um LED queime ou até mesmo exploda. 

Para obter o brilho máximo de um LED, você precisa encontrar o resistor correto para usar. Quando você compra um LED, pode consultar a sua especificação técnica, conhecido como datasheet para encontrar sua tensão direta forward voltage, e a sua corrente direta forward current.

A tensão é medida em Volts, cujo símbolo é V. E a corrente elétrica é medida em Amperes, cujo símbolo é A.

Por exemplo, caso o datasheet informe os seguintes valores para seu LED:
- forward voltage = 2,1 V (2,1 volts)
- forward current = 25 mA (25 miliamperes)

E sabendo que a tensão em volts (V) de fornecimento do Raspberry Pi Pico é de 3,3 V, você pode calcular o valor do resistor necessário utilizando a seguinte fórmula:

- Resistência Necessária = ( 3,3 V - forward voltage ) / forward current

A corrente direta (forward current em inglês) fornecida no datasheet está em miliamperes (mA). Antes de utilizar na fórmula, divida esse valor por 1000 para convertê-lo para a unidade de amperes (A), que é necessária para o cálculo.

Por exemplo, para os dados do LED acima, é necessário um resistor de pelo menos 48 Ω, conforme o cálculo que segue:

- Resistência Necessária = ( 3,3 V - 2,1 V ) / 0,025 A = 48 Ω

Seu resistor pode ser conectado a qualquer um dos pinos do seu LED, e depois ao seu Raspberry Pi Pico. Entretanto o LED só acenderá quando a eletricidade passar por ele na direção correta, do pino mais longo (ânodo) para o pino mais curto (cátodo). O pino mais curto do LED deve ser sempre conectado a um dos pinos `GND` do seu Raspberry Pi Pico.

### Fios de conexão com pinos e soquetes

Os fios de conexão, também conhecidos como jumpers, são usados para conduzir a corrente elétrica entre os componentes eletrônicos. Eles são utilizados em projetos de prototipagem porque permitem que você conecte e desconecte os componentes sem a necessidade de soldagem. A soldagem é um método que cria conexões permanentes ao fundir o metal.

Existem três tipos diferentes de fios de conexão:
- soquete-soquete, ou fêmea-fêmea (F-F)
- pino-soquete, ou macho-fêmea (M-F)
- pino-pino, ou macho-macho (M-M)

Cada tipo é identificado pelo que está colocado em cada extremidade do fio.

Uma extremidade do tipo pino possui um pequeno pedaço de metal saindo da extremidade de plástico preto. Essa extremidade pode ser inserida em um conector do tipo soquete ou em um orifício de uma placa de prototipagem.

![A extremidade de pino de um fio de conexão](/images/pin.png "A extremidade de pino de um fio de conexão")

A extremidade do tipo soquete parece uma pequena peça de plástico preto. Ela tem um orifício no interior que pode receber uma extremidade do tipo pino.

![A extremidade de soquete de um fio de conexão](/images/socket.png "A extremidade de soquete de um fio de conexão")

### Piscando um LED externo

Agora que você conhece os fundamentos da eletricidade, circuitos, e alguns componentes, está pronto para dar vida aos seus projetos com MicroPython! Será que você pode fazer um LED acender e apagar? Com certeza!

Use um resistor entre 50 e 330 ohms, um LED vermelho e um par de fios de conexão do tipo pino-pino e conecte esses componentes utilizando a placa de prototipagem conforme mostrado na imagem abaixo.

![LED e resistor conectados ao Pico](/images/single-led.png "LED e resistor conectados ao Pico")

Neste exemplo, o LED está conectado ao pino **GP15** do seu Raspberry Pi Pico. Se você usar um pino diferente, lembre-se de procurar o número no diagrama de pinos.

Use o mesmo código que você usou anteriormente para piscar o LED embarcado, mas mude o número do pino para 15.

```python
from machine import Pin, Timer

led = Pin(15, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
```

Programa 4.

Salve o seu programa no seu Raspberry Pi Pico com o nome de `blink1.py`. Execute o seu programa e o LED deverá começar a piscar. Se não estiver funcionando, verifique as conexões entre os componentes para ter certeza de que o LED está conectado corretamente.

Para ver este circuito em funcionamento no simulador Wokwi, clique [aqui](https://wokwi.com/projects/382840288712936449).