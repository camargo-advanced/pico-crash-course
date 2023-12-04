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

Logo abaixo da porta USB, encontra-se um botão identificado como `BOOTSEL`. Ele alterna entre os modos de inicialização ao ligar o Pico pela primeira vez, sendo útil para preparar o Pico para a programação com MicroPython.

Na parte inferior, três pinos dourados com a palavra `DEBUG` são destinados à depuração, isto é, à identificação de erros nos programas executados no Pico, usando uma ferramenta chamada debugger. Embora não seja explorado neste curso, pode ser útil ao lidar com programas mais complexos.

Ao girar o Pico, os rótulos nos pinos indicam suas funções principais, como `GP0`, `GP1`, `GND`, `VSYS`, `3V3` entre outros. Esses rótulos servem como referência, porém, ficam ocultos quando o Pico está inserido em uma placa de prototipagem (breadboard). O diagrama seguinte pode ser consultado para referência sempre que necessário. Mantenha-o por perto!

![Diagrama dos pinos do Pico](/images/pico-pinout-1.png "Diagrama dos pinos do Pico")

Perceba que um mesmo pino pode ter várias funções. Por exemplo, o pino `GP27` pode ser utilizado tanto como GPIO e PWM, sendo chamado de `GP27` nesses casos. Este mesmo pino também pode ser usado como ADC, sendo então referido como `ADC1`. Além disso, este pino pode desempenhar a função de I2C, sendo denominado `I2C1 SCL`. Em resumo, um único pino pode ser designado por vários nomes conforme a função que estiver sendo utilizada. Não se preocupe em compreender essas funções agora, pois as abordaremos em detalhes durante este curso. O importante é lembrar que um mesmo pino pode ser referenciado por mais de um nome ao longo desse curso.

Agora que você entendeu um pouco mais sobre o Raspberry Pi Pico, é possível perceber o incrível potencial dessa maravilha em miniatura. Este microcontrolador não só permite explorar os fundamentos da computação física, mas também representa uma entrada emocionante para o vasto mundo da programação.

Agora que você tem uma visão geral do hardware do Raspberry Pi Pico, está pronto para avançar para os próximos estágios deste emocionante curso. Não se esqueça de manter o diagrama dos pinos por perto para referência futura, pois será uma ferramenta valiosa ao explorar o Pico em profundidade.

Prepare-se para mergulhar em projetos práticos e emocionantes com o Raspberry Pi Pico. Estamos ansiosos para explorar ainda mais o potencial dessa incrível tecnologia com você!
