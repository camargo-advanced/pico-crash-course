## Projeto: LEDs piscando em sequência

E se agora você quiser que uma sequência de 3 LEDs pisque seuquencialmente e em uma frequência controlada pelo potenciômetro? Ao girar o potenciômetro a velocidade da sequência de LEDs aumenta ou diminui.

Mas antes de iniciarmos é necessária uma pausa para conhecermos um novo conceito em MicroPython chamado Listas que nos ajudará a alcançar nosso objetivo.

### Explorando Listas em Python

Imagine que você tem uma coleção de objetos, como números ou palavras, e quer organizá-los de uma forma que seja fácil de gerenciar. É aí que entram as listas!

Uma lista em Python é uma coleção de itens que podem ser de diferentes tipos, como números, palavras, objetos ou até mesmo outras listas. Cada item em uma lista tem uma posição única, que chamamos de índice. Para acessar um item em uma lista, basta usar o índice correspondente.

Aqui está um exemplo para ilustrar melhor:

```python
numeros = [10, 20, 30, 40, 50]
```

Neste caso, criamos uma lista chamada `numeros` que contém cinco números. Cada número tem um índice, começando do zero. Por exemplo, o primeiro número, 10, está no índice 0 da lista, o segundo número, 20, está no índice 1 e assim por diante.

Para acessar um item específico na lista, usamos o seu índice com a seguinte notação:

```python
primeiro_numero = numeros[0]  # Isso vai atribuir o valor 10 à variável primeiro_numero
segundo_numero = numeros[1]   # Isso vai atribuir o valor 20 à variável segundo_numero
```

Além disso, podemos modificar os itens em uma lista. Por exemplo, se quisermos mudar o segundo número para 25, podemos fazer assim:

```python
numeros[1] = 25  # Agora, a lista será [10, 25, 30, 40, 50]
```

E se quisermos adicionar um novo número à lista, usamos o método `append`:

```python
numeros.append(60)  # Agora, a lista será [10, 25, 30, 40, 50, 60]
```

E se quiser remover um item da lista, podemos usar o comando `del`:

```python
del numeros[2]  # Agora, a lista será [10, 25, 40, 50, 60]
```

As listas são muito úteis para organizar e manipular dados em Python. Elas nos permitem trabalhar com coleções de informações de forma eficiente. À medida que você avança em sua jornada na programação, vai descobrir que as listas são uma ferramenta poderosa e versátil em Python!

### O Loop `for` com Listas

O loop `for` é uma estrutura que permite iterar sobre os elementos de uma sequência. Uma sequência pode ser uma lista, uma tupla, uma string, ou qualquer outra coleção de elementos ordenados.

Ao percorrer uma lista usando um loop `for`, o código executa uma série de instruções para cada elemento da lista, em ordem.

Aqui está um exemplo para ilustrar:

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
```

Neste exemplo, temos uma lista chamada `numbers` que contém cinco elementos. O loop `for` está configurado para percorrer cada um desses elementos.

- Na primeira iteração, `number` terá o valor de 1 (o primeiro elemento da lista).
- Na segunda iteração, `number` terá o valor de 2 (o segundo elemento).
- E assim por diante, até a última iteração, onde `number` terá o valor de 5 (o último elemento).

Dentro do loop `for`, você pode realizar qualquer operação com o elemento atual. No exemplo acima, estamos apenas imprimindo o número, mas você poderia fazer qualquer coisa, como cálculos, operações de strings, entre outras coisas.

Essa capacidade de percorrer uma lista é fundamental porque permite que você automatize tarefas que envolvem uma coleção de elementos. Em vez de repetir o mesmo código para cada elemento individualmente, você pode usar um loop `for` para processar todos eles de uma vez.

Isso torna o código mais eficiente e legível. Além disso, facilita a manipulação de grandes conjuntos de dados.

### Implementando a sequência de LEDs

Voltando agora ao seu objetivo, você vai precisar de alguns componentes adicionais: 2 LEDs na cor que desejar, 2 resistores com valores entre `50` e `330 ohms` e 4 fios de conexão do tipo 'pino-pino', além de alguns dos componentes que já está utilizando. 

Conecte esses componentes utilizando a placa de prototipagem conforme mostrado na imagem que segue. 

![Imagem de circuito com 3 LEDs e potenciômetro](/images/led-seq-circuit.png "Imagem de circuito com 3 LEDs e potenciômetro")

Como exemplo, aqui está uma foto deste circuito montado. Observe como as conexões podem variar um pouco no mundo real.

![Imagem de circuito com 3 LEDs e potenciômetro](/images/led-seq-circuit-real.jpg "Imagem de circuito com 3 LEDs e potenciômetro")

Note que os LEDs estão conectados aos pinos `GP13`, `GP14` e `GP15` do Raspberry Pi Pico. Consulte o diagrama do Pico para confirmar a posição desses pinos. 

Note que existe um pino `GND` entre os pinos `GP13` e `GP14`. Consulte o diagrama do Pico para confirmar a posição desse pino. 

Cada um desses pinos tem um fio de conexão que os conecta com um resistor. A outra ponta de cada resistor está conectada a perna mais longa de cada LED. A outra perna de cada LED está conectada a outro fio de conexão que completa o circuito com o terra (GND). Dessa forma os elétrons vão fluir do pino do Pico, pelo fio até o resistor, passam através do LED emitindo luz, e então vão para o terra através de outro fio de conexão. 

> **`Atenção`**: Note que existem 3 fios de conexão conectados a trilha de terra da placa de prototipagem. Essa trilha está conectada a um dos pinos terra (GND) do Pico.

Adicione este código a um novo arquivo no Thonny, salve-o em seu Raspberry Pi Pico como `led-seq-pot.py` e depois execute-o. 

Para ver este circuito em funcionamento no simulador Wokwi, clique [aqui](https://wokwi.com/projects/382844312720112641).

```python
from machine import Pin, ADC
from time import sleep_ms

MAX_ADC_VALUE = 65535

leds = [Pin(13, Pin.OUT), Pin(14, Pin.OUT), Pin(15, Pin.OUT)]
pot = ADC(Pin(26))

while True:
    frequency_hz = int(pot.read_u16() / (MAX_ADC_VALUE/50)) + 1                                                                                                       
    period_ms = int((1000/frequency_hz) / (len(leds)*2)) 
    for led in leds:
        led.high()
        sleep_ms(period_ms)
        led.low()
        sleep_ms(period_ms)
```

Programa 9.

Vamos desvendar esse código linha por linha!

- `from machine import Pin, ADC`: Aqui estamos importando algumas funcionalidades muito importantes para o nosso projeto. Pin é usado para configurar e controlar os pinos do Raspberry Pi Pico. ADC nos permite ler o valor de um potenciômetro, que é uma espécie de controle giratório.

- `from time import sleep_ms`: Esta linha nos dá a capacidade de fazer o nosso programa "dormir" por um curto período de tempo, o que é útil para criar intervalos entre as ações.

- `MAX_ADC_VALUE = 65535`: Aqui, estamos definindo uma constante chamada `MAX_ADC_VALUE` com o valor 65535. Isso representa o valor máximo que o nosso potenciômetro pode ler.

- `leds = [Pin(13, Pin.OUT), Pin(14, Pin.OUT), Pin(15, Pin.OUT)]`: Aqui, criamos uma lista chamada `leds` com três objetos `Pin` conectados aos pinos `13` (GP13), `14` (GP14) e `15` (GP15) do Pico. Cada objeto `Pin` representa um LED, e eles estão configurados como saídas `OUT`, o que significa que podemos controlar se eles estão acesos ou apagados.

- `pot = ADC(Pin(26))`: Esta linha configura o pino `26` (ADC0) como um canal de leitura analógica usando o `ADC`. Em termos simples, isso nos permite ler a posição do potenciômetro.

- `while True:`: Agora, estamos entrando em um loop que vai executar o código indentado a ele infinitamente.

- `frequency_hz = int(pot.read_u16() / (MAX_ADC_VALUE/50)) + 1`: Esta linha lê a posição do potenciômetro e calcula uma frequência em Hertz. Em outras palavras, determina o quão rápido os LEDs irão piscar com base na posição do potenciômetro.

- `period_ms = int((1000/frequency_hz) / (len(leds)*2))`: Aqui, estamos calculando o período em milissegundos (quanto tempo os LEDs ficam acesos ou apagados). Isso é determinado pela frequência e pelo número de LEDs.

- `for led in leds:`: Este é um loop que percorre cada LED na lista leds e executa o código indentado para cada um desses LEDs.

- `led.high()`: Esta linha acende o LED. Quando o pino é configurado com nível alto de tesnão (high), ele fornece energia ao LED, fazendo-o acender.

- `sleep_ms(period_ms)`: Agora, estamos fazendo o programa esperar por um certo número de milissegundos (determinado pela variável `period_ms`). Isso determina quanto tempo o LED ficará aceso.

- `led.low()`: Agora, apagamos o LED. Quando o pino é configurado com nível baixo de tesnão (low), ele corta a energia para o LED, fazendo-o apagar.

- `sleep_ms(period_ms)`: Outra pausa para garantir que o LED permaneça apagado pelo mesmo período de tempo.

Essas linhas de código trabalham juntas para criar um efeito de piscar com os LEDs, e a velocidade desse piscar é controlada pelo potenciômetro. É incrível ver como podemos controlar o mundo físico com código, não é? Experimente ajustar o potenciômetro e veja como isso afeta o padrão de piscar dos LEDs!

Vocês já perceberam que, ao girar o potenciômetro para aumentar a velocidade dos LEDs ao máximo, algo curioso acontece? Parece que todos os LEDs estão sempre acesos, não é mesmo? Isso acontece porque, a partir de aproximadamente cerca de 50 Hz, o olho humano não consegue mais distinguir as piscadas individuais dos LEDs. Em vez disso, percebemos uma luz contínua. Isso se deve às características da visão humana, que tem uma capacidade limitada de perceber mudanças rápidas na luminosidade. É um exemplo fascinante de como a percepção visual humana pode ser influenciada por fatores físicos e biológicos.

> **`Atenção`**: Você pode conectar mais LEDs a essa sequência se desejar. Apenas adicione mais elementos `Pin` à lista `leds`. O restante do código não precisa ser alterado. E claro, não esqueça de ajustar o circuito físico com os novos LEDs e resistores conectados corretamente !

Continuem assim, você está fazendo um ótimo progresso!
