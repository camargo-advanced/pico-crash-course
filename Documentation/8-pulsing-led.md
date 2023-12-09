## Capítulo 8: Projeto Controle da intensidade do LED

Neste capítulo adentraremos o fascinante mundo da modulação por largura de pulso (PWM) para controlar a intensidade luminosa de um LED. Imagine a possibilidade de fazer um LED brilhar mais forte ou mais fraco, sem simplesmente ligá-lo e desligá-lo. Aqui, vamos explorar novos conceitos, como frequência, período, ciclo de trabalho e PWM, desvendando como cada um influencia a luminosidade do LED.

Imagine que exista uma forma de fazer um LED brilhar mais forte ou mais fraco, como se ele estivesse respirando devagar e rápido. Isso é ótimo porque não precisamos apenas ligar ou desligar o LED, podemos controlar o quão forte ele brilha.

Você fará isso daqui a pouco mas antes é necessário entender alguns conceitos novos tais como frequência e período, PWM e ciclo de trabalho (duty cycle in inglês) e como isso afeta a intensidade de um LED. 

### Frequência 

A frequência (Frequency em inglês) é como se mede a rapidez com que alguma coisa acontece de novo e de novo. Imagine um LED que se liga e desliga várias vezes em 1 segundo. Se isso acontece muitas vezes em pouco tempo, dizemos que tem uma alta frequência. Por exemplo, se um LED pisca 3 vezes por segundo, ele tem uma frequência 3 vezes mais alta que um LED que pisca 1 vez por segundo. A frequência é medida em Hertz (Hz), sendo que 1 Hz é igual a uma piscada do LED (acender e apagar) por segundo. No exemplo da figura o LED é ligado e desligado 3 vezes em 1 segundo. Logo, a frequência é de 3 Hz.

![Frequência, período e ciclo de trabalho](/images/pwm.png "Frequência, período e ciclo de trabalho")

### Período 

O período (Period em inglês) é o tempo que leva para algo acontecer uma vez. Se temos um LED piscando, o período é o tempo entre cada piscada. Por exemplo, se o LED pisca 3 vezes a cada 1 segundo, o período será de 1 segundo dividido por 3, ou seja 0,333 segundos, ou 333 milisegundos. Lembre que 1 segundo é igual a 1000 milisegundos.

### Ciclo de trabalho 

O ciclo de trabalho (Duty Cycle em inglês) é como se descreve o tempo que algo está ativo ou ligado durante um período. Imagine um LED piscando. Se ele fica aceso metade do tempo e apagado metade do tempo, dizemos que tem um ciclo de trabalho de 50%. Se ele fica aceso por mais tempo do que apagado, o ciclo de trabalho é maior. 

Agora, olhe para o figura que mostra 3 períodos de um sinal de 3 Hz e analise os diferentes ciclos de trabalho e como eles afetam o tempo em que o LED fica ligado e desligado:

- 0% Duty Cycle: Neste caso, o LED está sempre apagado. Não importa quantos períodos passem, ele nunca fica ligado. 

- 25% Duty Cycle: Aqui, o LED está ligado por um quarto do período e apagado por três quartos. Isso significa que o LED fica aceso por um curto tempo e depois apagado por um tempo mais longo.

- 50% Duty Cycle: Com um ciclo de trabalho de 50%, o LED está ligado por metade do período e apagado pela outra metade. É como um LED piscando que passa a mesma quantidade de tempo aceso e apagado.

- 75% Duty Cycle: Neste caso, o LED está ligado por três quartos do período e apagado por um quarto. Ele fica aceso por mais tempo do que fica apagado.

- 100% Duty Cycle: Aqui, o LED está sempre ligado. Não importa quanto tempo passe, ele nunca se apaga.

### Modulação por largura de pulso 

Modulação por largura de pulso (PWM, Pulse Width Molulation em inglês), é uma técnica utilizada para controlar a quantidade de energia entregue a um componente, como um LED. Ao invés de simplesmente ligar ou desligar, o PWM liga e desliga muito rapidamente em uma sequência, sendo que a cada tempo ele pode utilizar um ciclo de trabalho (duty cycle) diferente. Isso cria a ilusão de que o componente está operando em um nível intermediário de intensidade.

### LED pulsando em 3 Hz

Agora que você já entendeu esses conceitos, imagine fazer um código que faça um LED piscar em 3 Hz e além disso pulsar como um coração? Você fará isso acendendo e desligando o LED a cada período, só que gradualmente através da alteração do ciclo de trabalho (duty cycle) a cada milisegundo usando o PWM do seu Raspberry Pi Pico. 

Primeiramente monte o circuito do jogo colocando um led vermelho no pino GP15 do seu Raspberry Pi Pico. Lembre de colocar um resistor para limitar a corrente conforme discutido em exemplos anteriores, como por exemplo, um resistor de 220 Ohms.

Uma forma de montar esse circuito segue na figura que segue. Fique a vontade para ajustar o circuito de acordo com o que for mais conveniente para você!

![Circuito do jogo da reação](/images/pulse-circuit.png "Circuito do jogo da reação")

Abra um novo arquivo no editor Thonny e adicione o seguinte código.

```python
from machine import Pin, PWM
from time import sleep_ms

MAX_DUTY_VALUE = 65535 

pwm = PWM(Pin(15))
pwm.freq(500)

frequency_hz = 3
period_ms = int((1/frequency_hz) * 1000)
duty_inc_per_ms = int(MAX_DUTY_VALUE / (period_ms/2))

while True:
    for duty in range(0, MAX_DUTY_VALUE, duty_inc_per_ms):
        pwm.duty_u16(duty)
        sleep_ms(1)

    for duty in range(MAX_DUTY_VALUE, 0, -duty_inc_per_ms):
        pwm.duty_u16(duty)
        sleep_ms(1)
```

Programa 8.1

Depois de escrever o código, salve-o no Raspberry Pi Pico com o nome `pulse.py` e execute. Vai ser legal ver o LED pulsar e brilhar continuamente de uma forma especial!

Se quiser, você pode mexer nas configurações para mudar o ritmo e a intensidade do brilho do LED. É como ajustar a música para que ela toque mais rápido ou mais devagar, mas com luzes!

Para ver este circuito em funcionamento no simulador Wokwi, clique [aqui](https://wokwi.com/projects/382848966469555201).

Segue a explicação de cada parte do código para você entender melhor.

```python
from machine import Pin, PWM
from time import sleep_ms
```

- `from machine import Pin, PWM`: Isso importa as funcionalidades de controle de pinos (Pin) e Modulação por Largura de Pulso (PWM) da biblioteca `machine`, que nos permite interagir com componentes eletrônicos.
- `from time import sleep_ms`: Isso importa a função `sleep_ms` da biblioteca `time`, que nos permite pausar o programa por um número especificado de milissegundos.

```python
MAX_DUTY_VALUE = 65535
```

- `MAX_DUTY_VALUE` é uma constante que representa o valor máximo de intensidade luminosa que o LED pode atingir. Este valor é específico para o hardware e pode variar de acordo com o microcontrolador. Em MicroPython usamos nomes de variáveis em maiúsculo para representar valores constantes.

```python
pwm = PWM(Pin(15))
pwm.freq(500)
```

- `pwm = PWM(Pin(15))`: Aqui, estamos configurando o pino GP15 como uma saída PWM (Modulação por Largura de Pulso) e associando isso à variável chamada `pwm`.

- `pwm.freq(500)`: Estamos definindo a frequência do sinal PWM como 500 Hz (ciclos por segundo). Isso significa que o LED irá ligar e desligar 500 vezes por segundo.

```python
frequency_hz = 3
period_ms = int((1/frequency_hz) * 1000)
duty_inc_per_ms = int(MAX_DUTY_VALUE / (period_ms/2))
```

- `frequency_hz = 3`: Aqui, estamos definindo a frequência desejada do pulsar em 3 Hz, ou seja, o LED vai pulsar 3 vezes por segundo.

- `period_ms = int((1/frequency_hz) * 1000)`: Calculamos o período em milissegundos usando a fórmula (1/frequency_hz) * 1000. O período é o tempo que leva para o ciclo de trabalho se repetir.

- `duty_inc_per_ms = int(MAX_DUTY_VALUE / (period_ms/2))`: Aqui, estamos calculando quanto o ciclo de trabalho (duty cycle) deve aumentar a cada milissegundo para alcançar a frequência desejada. Dividimos o valor máximo do ciclo de trabalho pela metade do período em milissegundos porque em 1 período temos que fazer duas coisas: primeiro aumentar a intensidade do LED até o máximo brilho e depois na outra metade do período, temos que reduzir a intensidade do LED até chegar em zero, ou seja, LED apagado.

```python
while True:
    for duty in range(0, MAX_DUTY_VALUE, duty_inc_per_ms):
        pwm.duty_u16(duty)
        sleep_ms(1)

    for duty in range(MAX_DUTY_VALUE, 0, -duty_inc_per_ms):
        pwm.duty_u16(duty)
        sleep_ms(1)
```

- `while True:`: Inicia um loop infinito. Todo o código dentro deste loop será executado repetidamente.

- `for duty in range(0, MAX_DUTY_VALUE, duty_inc_per_ms):`: Este loop percorre uma série de valores de `0` até o `MAX_DUTY_VALUE`, aumentando de acordo com `duty_inc_per_ms`. `duty` representa o novo ciclo de trabalho.

- `pwm.duty_u16(duty)`: Altera o ciclo de trabalho do PWM para o valor atual de `duty`.

- `sleep_ms(1)`: Espera por 1 milissegundo. Isso controla a velocidade com que o ciclo de trabalho é alterado, influenciando na frequência do pulsar.

- O segundo loop `for duty in range(MAX_DUTY_VALUE, 0, -duty_inc_per_ms)` faz o mesmo, mas em ordem reversa, para criar o efeito de pulsar. Note o sinal de menos antes da variável `duty_inc_per_ms`. Dessa forma informamos ao laço `for` que ele deve decrementar aquele valor a cada iteração.

Experimente brincar com os valores de frequência, ciclo de trabalho, assim como o tempo de espera (sleep), para ter uma ideia de como você pode ajustar a intensidade e o ritmo do LED pulsante.

### Exercícios

#### Exercício 8.1: Pulsar do LED

Escreva um código que faça o LED pulsar a uma frequência de 5 Hz.

Experimente diferentes valores de ciclo de trabalho para variar a intensidade do brilho durante o pulsar.

#### Exercício 8.2: Frequência Variável do LED

Escreva um código que permita variar a frequência do pulsar do LED de 2 Hz para 10 Hz em intervalos de 2 Hz.

Execute o código e observe como a mudança na frequência afeta a percepção visual do LED.

### Conclusão

Compreendemos agora a importância da frequência, do período e do ciclo de trabalho na manipulação da intensidade luminosa de um LED utilizando a técnica de modulação por largura de pulso (PWM). Ao explorar esses conceitos, pudemos visualizar o efeito do PWM, permitindo que o LED pulsasse com diferentes níveis de brilho.

Ao programar o Raspberry Pi Pico para realizar esse efeito pulsante, aprendemos a configurar o pino PWM, definir a frequência desejada e manipular o ciclo de trabalho para controlar o brilho do LED. Ao ajustar esses parâmetros, foi possível criar um efeito pulsante semelhante a um coração batendo, adicionando dinamismo e vida ao LED.

Continue explorando, experimentando e transformando suas ideias em realidade por meio da eletrônica e programação. O universo da modulação por largura de pulso é vasto e cheio de possibilidades, e agora você está equipado para explorá-lo e criar projetos cada vez mais interessantes e desafiadores.
