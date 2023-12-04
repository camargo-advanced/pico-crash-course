## Projeto: Acendendo e piscando o LED embarcado

No capítulo anterior você explorou a base essencial da programação em Python com um simples "Hello, World!", um marco simbólico para iniciantes em linguagens de programação.

Agora você dará um salto empolgante na direção da verdadeira magia da computação física! Vamos sair do mundo abstrato do código para o universo tangível dos dispositivos eletrônicos. Este capítulo marca o verdadeiro "Hello, World" da computação física: vamos controlar um LED!

O MicroPython adiciona bibliotecas específicas de hardware, como `machine`, que você pode usar para programar o seu Raspberry Pi Pico. Vamos criar um objeto `machine.Pin` para acessar o LED embarcado conectado ao pino `GP25` do seu Pico.

Digite o seguinte código no painel do Shell, e certifique-se de pressionar `Enter` após cada linha.

```Python
from machine import Pin

led = Pin(25, Pin.OUT)
led.value(1)
```

Programa 1.

Se você definir o valor do LED como 1, ele se acende. Dessa forma você deverá ver o LED embarcado se acender. Confirme isso localizando o LED embarcado em seu Pico. 

Embarcado neste contexto significa que o LED faz parte da placa do próprio Raspberry Pi Pico. É como aquela luzinha que já vem junto com a sua televisão e indica se ela está ligada. Portanto, o LED embarcado do Raspberry Pi Pico se refere ao LED que está diretamente conectado e vem junto com o próprio Raspberry Pi Pico.

Agora digite o seguinte código para definir o valor como 0 e desligar o LED embarcado. Não esqueça de pressionar `Enter` ao final para executar o comando.

```Python
led.value(0)
```

Uma dica valiosa para tornar os códigos mais intuitivos é substituir `led.value(1)` por `led.high()` nos exemplos anteriores. Da mesma forma, `led.value(0)` pode ser substituído por `led.low()`. Essas alterações podem tornar os comandos mais claros e fáceis de compreender. A escolha é sua!

Experimente ligar e desligar o LED quantas vezes desejar.

> **`Atenção`**: Você pode usar a seta para cima no teclado para acessar rapidamente linhas de código anteriores e então pressionar o botão `Enter` do seu teclado para executá-las.

### Salvando o programa em um arquivo .py

Apesar de ser vantajoso utilizar o painel de Shell para realizar testes de código de forma rápida e interativa, se você deseja escrever um programa mais longo é melhor salvá-lo em um arquivo para poder reutilizá-lo mesmo após reiniciar seu Pico.

O Thonny pode salvar e executar programas MicroPython diretamente no seu Raspberry Pi Pico. Para testar isso você irá criar um programa em MicroPython para fazer o LED embarcado alternar entre ligado e desligado.

Clique no painel principal do editor do Thonny localizado na parte superior da tela. Digite o seguinte código para alternar o LED.

```Python
from machine import Pin

led = Pin(25, Pin.OUT)
led.toggle()
```

Programa 2.

A primeira linha de código `from machine import Pin` importa uma biblioteca do MicroPython chamada `machine` que contém funções para interagir com hardware. Mais especificamente, ela está importando a função `Pin`, que permite controlar os pinos do Raspberry Pi Pico.

Na segunda linha `led = Pin(25, Pin.OUT)` é criada uma variável chamada `led`. Esta variável é configurada para controlar o pino `GP25` do Raspberry Pi Pico, que está conectado ao LED embarcado da placa. A segunda parte `Pin.OUT` significa que este pino será usado para enviar um sinal de saída, como acender ou apagar um LED.

A última linha `led.toggle()` está dizendo para o LED trocar de estado. Se o LED estiver aceso, ele será apagado, e vice-versa.

![Alternando o LED embarcado entre ligado e desligado](/images/thonny-led-toggle.png "Alternando o LED embarcado entre ligado e desligado")

Clique em `File -> Save as...` para salvar seu programa. O Thonny perguntará se você deseja salvar o arquivo em seu computador 'This computer' ou em seu Raspberry Pi Pico. Escolha 'Raspberry Pi Pico'. 

![Salvando o arquivo no Pico](/images/this-computer-or-pico.png "Salvando o arquivo no Pico")

Digite 'blink.py' como o nome do arquivo.

> **`Atenção`**: Você precisa incluir a extensão `.py` para que o Thonny reconheça o arquivo como um arquivo MicroPython.

Agora clique no botão `Run` para executar seu código. Você deverá ver o LED embarcado alternar entre ligado e desligado a cada vez que clicar no botão `Run`.

### A biblioteca Timer

Você pode usar a biblioteca `Timer` para configurar um temporizador que executa uma função em intervalos regulares.

Adicione este código a um novo arquivo no Thonny, e salve-o em seu Raspberry Pi Pico como `blink2.py` e depois execute-o. 

```Python
from machine import Pin, Timer

led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
```

Programa 3.

A seguir, vamos entender esse código linha a linha.

- `from machine import Pin, Timer`: nessa linha estamos importando a função `Timer` da biblioteca `machine` que permite configurar e gerenciar temporizadores.

- `timer = Timer()`: essa linha cria um objeto chamado `timer`. Este objeto será usado para configurar um temporizador que irá chamar uma função customizada em MicroPython em intervalos regulares.

- `def blink(timer)`: essa linha declara uma função em MicroPython. Uma função é um conjunto de instruções que podem ser usadas repetidamente. No caso, esta função tem o nome `blink` e recebe um parâmetro chamado `timer`. `def` é uma palavra-chave importante em MicroPython que é usada para definir, ou declarar, funções. A sintaxe de MicroPython exige que se coloque dois pontos `:` no final da linha de declaração da função. Funções são parte fundamental da programação, permitindo a organização e reutilização de código.

Uma parte importante aqui é a indentação. A indentação refere-se aos espaços ou tabulações que são usados no início das linhas para organizar o código. Em MicroPython, a indentação é muito importante fazendo parte da linguagem e é usada para indicar quais instruções estão dentro de um bloco de código. Utilize sempre 'espaços em branco' para indentar seu código. Não utilize `TAB`.

No exemplo dado, a linha `led.toggle()` está indentada. Isso significa que ela faz parte do bloco de código da função `blink`. Ou seja, quando a função `blink` é chamada, o programa executa `led.toggle()` como parte dessa função. Se `led.toggle()` não estivesse indentada, o MicroPython não entenderia que ela faz parte da função `blink`. A indentação é como uma forma de dizer ao MicroPython quais partes do código pertencem a uma função.

- `timer.init`: essa linha inicializa o temporizador que criamos anteriormente. Ele é configurado para uma frequência de 2,5 Hz `freq=2.5`, ou seja, a função `blink` será chamada 2,5 vezes por segundo, com o modo de operação `Timer.PERIODIC`, significando que o temporizador irá chamar a função repetidamente e indefinidamente. O `callback=blink` indica que a função a ser chamada é a função `blink` definida anteriormente.

O conceito de frequência, em termos simples, se refere a quantas vezes algo acontece em um determinado intervalo de tempo. No contexto do temporizador, isso significa quantas vezes ele executa uma ação específica dentro do intervalo de 1 segundo. Neste caso, a frequência é 2,5 vezes por segundo, o que significa que a função `blink` será chamada 2,5 vezes a cada segundo. Se você definisse a frequência como 0,5, o LED piscaria apenas a cada dois segundos, o que seria mais devagar. 

> **`Zen do MicroPython`**: Fique calmo: mais adiante explicaremos em detalhes o conceito de frequência assim como outros conceitos relacionados. 

Em programas MicroPython, lembre-se de utilizar o padrão norte-americano para valores decimais. Nele, o separador decimal é o ponto '.', e não a vírgula ','. Por exemplo, o número 0,5 deve ser escrito como 0.5 no código em MicroPython.

Clique no botão `Run` e o seu programa fará o LED piscar até que você clique no botão `Stop`. 

Parabéns por concluir com sucesso nosso primeiro projeto de computação física com MicroPython! Ao acender e piscar um LED, você deu um passo significativo na compreensão da conexão entre o código que escrevemos e a ação real que acontece no mundo físico.

Este projeto pode parecer simples, mas é um marco importante no seu caminho na programação. Você experimentou o poder de transformar comandos de código em ações tangíveis. Esse LED que brilha agora é apenas o começo de uma série de projetos incríveis que você poderá criar com o MicroPython.

Parabéns novamente e até o próximo capítulo, repleto de mais aventuras emocionantes na programação com MicroPython!
