## Projeto: Dimmer 

Neste capítulo, mergulharemos no emocionante mundo dos potenciômetros e da leitura de sinais analógicos com o Raspberry Pi Pico. Compreenderemos como um potenciômetro, esse dispositivo tão versátil, pode atuar como uma ferramenta valiosa para controlar a intensidade luminosa de um LED.

O potenciômetro, um componente analógico, é como uma torneira em um encanamento elétrico, permitindo-nos regular o fluxo de eletricidade. Ao girá-lo, podemos ajustar a quantidade de energia que flui pelo circuito, influenciando diretamente no brilho do LED. Esta é uma oportunidade emocionante de explorar como componentes analógicos podem ser integrados ao universo digital do Raspberry Pi Pico.

### O que é um Potenciômetro?

O potenciômetro é um componente muito útil na eletrônica. Pode ser um pouco difícil de pronunciar, mas é fácil de entender! 

Vamos imaginar um potenciômetro como uma torneira de água em um encanamento. A imagem que segue mostra um potenciômetro típico.

![Potenciômetro conectado com um LED ao Pico](/images/potentiometer.jpg "Potenciômetro conectado com um LED ao Pico")

Imagine que temos um cano por onde a água (eletricidade) pode fluir. O potenciômetro é como uma torneira nesse cano (circuito). Girando a torneira, podemos controlar o fluxo de água através do encanamento (fluxo de elétrons pelo circuito).

Se abrimos a torneira completamente, a água flui livremente. Mas, se giramos a torneira para um ponto intermediário, a água encontra mais resistência e flui mais devagar. Se fecharmos a torneira o fluxo de água cessa.

Se ligarmos um LED a esse circuito, podemos controlar o brilho dele girando a torneira. Quanto mais resistência (torneira mais fechada), menos eletricidade passa e a lâmpada fica mais fraca. Se abrimos totalmente, a lâmpada brilha forte.

Dessa forma o potenciômetro atua como uma torneira no nosso encanamento elétrico, controlando o fluxo de eletricidade. Isso nos dá a capacidade de ajustar o funcionamento de dispositivos elétricos com mais precisão.

### Conversor Analógico-Digital 

Um Conversor Analógico-Digital (ADC, Analog-to-Digital Converter em inglês), é como um tradutor que transforma coisas que são contínuas, como luz, som ou temperatura, em números para que um computador pode entender. É como quando você mede algo com uma régua e anota o número para saber o tamanho.

Isso é muito útil porque os computadores entendem apenas números, mas o mundo ao nosso redor é cheio de coisas que não são números diretamente. Com um ADC, podemos medir e usar esses valores em nossos projetos com Raspberry Pi Pico.

Por exemplo, o ADC pode ler um potenciômetro e traduzir essa leitura em valor entre 0 e 65535. Esse valor pode ser utilizado para definir o ciclo de trabalho (_duty cycle_) em um PWM para controlar a intensidade de um LED, que também opera na mesma faixa de valores.

### Lendo valores de um Potenciômetro

Substitua o botão no seu circuito por um potenciômetro. Siga o diagrama abaixo para conectá-lo ao pino analógico `GP26`.

![Potenciômetro conectado ao Pico](/images/pot-circuit.png "Potenciômetro conectado ao Pico")

Adicione este código a um novo arquivo no Thonny, salve-o em seu Raspberry Pi Pico como `pot.py` e depois execute-o. 

Para ver este circuito em funcionamento no simulador Wokwi, clique [aqui](https://wokwi.com/projects/382841403521287169).

```python
from machine import ADC, Pin
from time import sleep_ms

adc = ADC(Pin(26))

while True:
    print(adc.read_u16())
    time.sleep_ms(5)
```

Programa 7.

A seguir a explicação das linhas mais importantes do código.

- `from machine import ADC, Pin`: A novidade aqui é que estamos importando a função `ADC` da biblioteca `machine`, que nos ajudará a ler o potenciômetro.

- `from time import sleep_ms`: importa a função `sleep_ms` que faz com que a execução do programa pause por um período de tempo especificado em milisegundos.

- `adc = ADC(Pin(26))`: Nessa linha estamos criando um objeto ADC conectado ao pino 26 (`ADC0`) do Raspberry Pi Pico, ou seja, estamos dizendo ao Raspberry Pi Pico para usar o pino para 'escutar' o potenciômetro. Pense nisso como conectar um ouvido (o pino) para ouvir o potenciômetro.

- `print(adc.read_u16())`: Esta linha lê a posição do potenciômetro e converte em um número que é impresso no Shell.

- `time.sleep_ms(5)`: pausa o programa por 5 milisegundos.

Agora gire o potenciômetro para ver seus valores máximo e mínimo. Eles devem estar aproximadamente entre 0 e 65535. 

> **`Atenção`**: Caso tenha pequenas variações nos valores mínimo e máximo lidos do potenciômetro pode ser devido a qualidade do componente. Mas não se preocupe, pequenas variações não vão atrapalhar nesse caso.

O Thonny tem uma opção chamada Plotter que permite que você exiba os valores impressos no Shell de forma gráfica. Isso pode ajudar a entender melhor o efeito ao girar o botão do potenciômetro. No Thonny, escolha 'View > Plotter' e a janela do plotter aparecerá ao lado direito do Shell.

![Imagem animada do plotter](/images/thonny-plotter.gif "Imagem animada do plotter")

Gire novamente o potenciômetro e veja a alteração dos valores no Plotter. É possível ver a linha subir a medida que você 'abre mais a torneira' do potenciômetro, e vice-versa.

E porque não usar esse valor para controlar o ciclo de trabalho do PWM e dessa forma controlar a intensidade do LED?

Primeiramente monte o circuito do jogo colocando um led vermelho no pino GP15 do seu Raspberry Pi Pico. Lembre de colocar um resistor para limitar a corrente conforme discutido em exemplos anteriores, como por exemplo, um resistor de 220 Ohms.

Uma forma de montar esse circuito segue na figura que segue. Fique a vontade para ajustar o circuito de acordo com o que for mais conveniente para você!

![Potenciômetro conectado ao Pico](/images/pot-and-led.png "Potenciômetro conectado ao Pico")

Altere o código anterior conforme segue, e salve-o no Raspberry Pi Pico como `pot-led.py`. Uma vez que você o tenha executado, ajuste o botão do potenciômetro para controlar a intensidade do LED.

Para ver este circuito em funcionamento no simulador Wokwi, clique [aqui](https://wokwi.com/projects/382842211410367489).

```python
from machine import Pin, PWM, ADC
from time import sleep_ms

pwm = PWM(Pin(15))
adc = ADC(Pin(26))

pwm.freq(1000)

while True:
    duty = adc.read_u16()
    pwm.duty_u16(duty)
    sleep_ms(5)
```

Programa 8.

Exploramos o papel fundamental do potenciômetro como uma valiosa ferramenta para controlar o brilho de um LED através da leitura de sinais analógicos. Compreendemos sua analogia com uma torneira, regulando o fluxo de eletricidade e, consequentemente, a intensidade luminosa do LED.

Ao substituir o botão por um potenciômetro em nosso circuito, conseguimos ler seus valores de resistência. Com a ajuda do conversor analógico-digital (ADC), traduzimos esses valores em números compreensíveis para o Raspberry Pi Pico, permitindo-nos controlar o ciclo de trabalho do PWM e, consequentemente, a luminosidade do LED.

Ao ajustar o código e conectar o potenciômetro ao LED, experimentamos a capacidade de controlar o brilho do LED girando o potenciômetro. Esse controle dinâmico adiciona uma dimensão interativa e prática aos projetos eletrônicos, destacando o potencial dos componentes analógicos na era digital.

Com este conhecimento, você está pronto para explorar novas possibilidades e criar projetos ainda mais interessantes, manipulando sinais analógicos e integrando-os ao seu mundo digital. O potenciômetro é apenas o começo de suas aventuras eletrônicas com o Raspberry Pi Pico. Aproveite essa jornada emocionante e continue explorando o vasto e fascinante campo da eletrônica e da programação.
