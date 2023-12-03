## O que é o Raspberry Pi Pico?
O Raspberry Pi Pico é uma maravilha em miniatura, colocando a mesma tecnologia que sustenta desde sistemas de casa inteligente até fábricas industriais na palma da sua mão. Esteja você interessado em aprender sobre a linguagem de programação MicroPython, dando os primeiros passos na computação física, ou deseja construir um projeto de hardware, o Raspberry Pi Pico pode lhe apoiar em cada etapa do caminho.

O Raspberry Pi Pico é conhecido como uma placa de desenvolvimento de microcontrolador, o que significa simplesmente que é uma placa de circuito impresso que abriga um tipo especial de processador projetado para contato com o mundo físico: o microcontrolador. Do tamanho de um pedaço de goma de mascar, o Raspberry Pi Pico possui uma surpreendente quantidade de potência graças ao chip no centro da placa: um microcontrolador RP2040.

O Raspberry Pi Pico não foi projetado para substituir o computador que você tem em casa, que pertence a uma classe diferente de dispositivo conhecido como computador pessoal (PC, Personal Computer em inglês). Enquanto você pode usar o seu PC para jogar jogos, escrever histórias e navegar na web, o Raspberry Pi Pico foi projetado para projetos de computação física onde ele controla desde LEDs e botões até sensores, motores e até mesmo outros microcontroladores. 

Ao longo deste curso, você aprenderá muito sobre o Raspberry Pi Pico, mas as habilidades que você adquirir também se aplicarão a qualquer outra placa de desenvolvimento baseada no microcontrolador RP2040, e até mesmo a outros dispositivos, contanto que sejam compatíveis com a linguagem de programação MicroPython.

### Vamos conhecer o hardware do Pico?
O Raspberry Pi Pico é um dispositivo compacto com uma variedade de recursos acessíveis por meio dos pinos dispostos ao redor da placa. Nas bordas mais longas, destacam-se seções douradas - esses são os pinos que conectam o microcontrolador RP2040 ao mundo exterior, conhecidos como Entrada/Saída (I/O, Input/Output em inglês).

![Raspberry Pi Pico visto de cima](/images/pico-top.png "Raspberry Pi Pico visto de cima")

O chip no centro do Pico é o microcontrolador RP2040, um Circuito Integrado (CI) personalizado, projetado para fornecer potência computacional ao Pico e a outros dispositivos baseados em microcontroladores. Contra a luz, é possível ver o logotipo da Raspberry Pi gravado no topo do chip, acompanhado por letras e números que identificam a origem e o fabricante do chip.

Na parte superior do Pico, há uma porta micro USB. Ela fornece energia e permite a comunicação do Pico com um computador, possibilitando o carregamento de programas. Esta porta é mais estreita na parte inferior e mais larga na superior, semelhante ao conector do cabo micro USB.

> **`Atenção`**: O cabo micro USB só se encaixará na porta micro USB do seu Pico de uma maneira. Ao conectá-lo, certifique-se de alinhar os lados estreito e largo da maneira correta ou você pode danificar o seu Pico ao tentar forçar o cabo micro USB na direção errada!

Logo abaixo da porta USB, encontra-se um botão identificado como **BOOTSEL**. Ele alterna entre os modos de inicialização ao ligar o Pico pela primeira vez, sendo útil para preparar o Pico para a programação com MicroPython.

Na parte inferior, três pinos dourados com a palavra **DEBUG** são destinados à depuração, isto é, à identificação de erros nos programas executados no Pico, usando uma ferramenta chamada debugger. Embora não seja explorado neste curso, pode ser útil ao lidar com programas mais complexos.

Ao girar o Pico, os rótulos nos pinos indicam suas funções principais, como **GP0**, **GP1**, **GND** **VSYS**, **3V3** entre outros. Esses rótulos servem como referência, porém, ficam ocultos quando o Pico está inserido em uma placa de prototipagem (breadboard). O diagrama seguinte pode ser consultado para referência sempre que necessário. Mantenha-o por perto!

![Diagrama dos pinos do Pico](/images/pico-pinout-1.png "Diagrama dos pinos do Pico")

Perceba que um mesmo pino pode ter várias funções. Por exemplo, o pino `GP27` pode ser utilizado tanto como GPIO e PWM, sendo chamado de `GP27` nesses casos. Este mesmo pino também pode ser usado como ADC, sendo então referido como `ADC1`. Além disso, este pino pode desempenhar a função de I2C, sendo denominado `I2C1 SCL`. Em resumo, um único pino pode ser designado por vários nomes conforme a função que estiver sendo utilizada. Não se preocupe em compreender essas funções agora, pois as abordaremos em detalhes durante este curso. O importante é lembrar que um mesmo pino pode ser referenciado por mais de um nome ao longo desse curso.

Se você tiver uma placa de prototipagem, insira o seu Raspberry Pi Pico na placa de forma que ele cubra a divisão do meio e a porta micro USB esteja no topo da placa, conforme a figura que segue. Empurre delicadamente o Pico para baixo até que as partes plásticas dos pinos estejam tocando a placa de prototipagem. Isso significa que as partes metálicas dos pinos estão totalmente inseridas e fazendo um bom contato elétrico com a placa de prototipagem.

O pino superior esquerdo, **GP0**, deve estar na fileira marcada com um **1**, se sua placa de prototipagem estiver numerada (algumas placas iniciam pelo valor **0**). Antes de empurrar o seu Pico para baixo, certifique-se de que os pinos estejam todos devidamente posicionados. Se você dobrar um pino, pode ser difícil endireitá-lo novamente sem quebrá-lo.

![Pico inserido na placa de prototipagem](/images/pico-breadboard.png "Pico inserido na placa de prototipagem")

> **`Atenção`**: Insira o Pico com o conector micro USB posicionado para o topo da placa de prototipagem conforme a figura. Isso facilitará a conexão do cabo micro USB posteriormente.

Agora conecte o seu cabo micro USB à porta localizada no lado esquerdo do Pico.

![Conectando cabo micro usb ao Pico](/images/micro-usb-pico.png "Conectando cabo micro usb ao Pico")

> **`Atenção`**: Seja gentil ao conectar o cabo micro USB ao seu Pico. O conector do Pico é frágil e pode danificar facilmente. Após fixar o cabo, evite retirá-lo com frequência.

## Programando com MicroPython
Desde o seu lançamento em 1991, a linguagem de programação Python, nomeada após a famosa série de televisão **Monty Python**, cresceu para se tornar uma das mais populares no mundo. Sua popularidade, no entanto, não significa que não haja melhorias que possam ser feitas especialmente se você estiver trabalhando com um microcontrolador. 

A linguagem de programação Python foi desenvolvida para sistemas de computador como desktops, laptops e servidores. Placas de microcontrolador como o Raspberry Pi Pico são menores, mais simples e têm consideravelmente menos memória, o que significa que não conseguem executar a mesma linguagem Python que seus equivalentes maiores.

É aqui que o MicroPython entra em cena. Originalmente desenvolvido por **Damien George** e lançado pela primeira vez em 2014, o MicroPython é uma linguagem de programação compatível com Python desenvolvida especificamente para microcontroladores. Ele inclui muitas das características do Python convencional, enquanto adiciona uma variedade de novas funcionalidades projetadas para aproveitar as facilidades disponíveis no Raspberry Pi Pico e em outras placas de microcontrolador. Se você já programou em Python antes, encontrará o MicroPython imediatamente familiar. Se não, não se preocupe: é uma linguagem fácil de aprender!

### Thonny Python IDE
O **Thonny** é um ambiente de desenvolvimento integrado (IDE, Integrated Development Environment em inglês) para a linguagem de programação Python. Ele é projetado especialmente para iniciantes e estudantes de programação. O Thonny oferece uma interface de usuário simples e intuitiva, o que o torna mais fácil de usar para aqueles que estão aprendendo a programar em Python.

Algumas das características do Thonny incluem:
- **Editor de código**: possui um editor de código com destaque de sintaxe, sugestões de código e outras funcionalidades para facilitar a escrita de código Python.
- **Shell integrado**: possui um shell Python integrado, permitindo que os usuários testem rapidamente pequenos trechos de código sem a necessidade de criar um arquivo Python separado.
- **Depurador simples**: oferece funcionalidades de depuração para ajudar a identificar e corrigir erros no código.
- **Explorador de variáveis**: permite visualizar o estado das variáveis durante a execução do programa.
- **Gerenciador de pacotes integrado**: Facilita a instalação e gerenciamento de bibliotecas e pacotes Python.
- **Suporte a placas microcontroladoras**: Thonny é compatível com microcontroladores como o Raspberry Pi Pico, o que facilita a programação de dispositivos embarcados.

No geral, o Thonny é uma escolha popular para iniciantes em Python devido à sua interface amigável e às ferramentas úteis que oferece para facilitar o aprendizado da linguagem de programação e de desenvolvimento de sistemas computação física.

A seguir você irá instalar o Thonny, irá se conectar ao seu Raspberry Pi Pico e também executar um código Python simples usando o Shell.
