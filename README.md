# Introdução à MicroPython com Raspberry Pi Pico

Bem vindo!
Você associa computadores àquelas máquinas que ficam na sua mesa e você digita nelas? Isso certamente é um tipo de computador, mas não é o único. Neste curso, estamos explorando microcontroladores - pequenas unidades de processamento com menos memória, especializadas em controlar outros dispositivos. 

Com certeza você já tem vários microcontroladores em casa. A sua TV, por exemplo, muito provavelmente é controlada por um microcontrolador; o mesmo pode ocorrer com a sua máquina de café ou no micro-ondas. É claro que todos esses microcontroladores já vêm com seus próprios programas e os fabricantes tornam difícil alterar o software que está rodando neles.

Por outro lado, um Raspberry Pi Pico pode ser facilmente reprogramado através de uma conexão USB. Neste curso vamos aprender como utilizar esse hardware e como trabalhar com outros componentes eletrônicos. Ao final desta jornada, você terá a habilidade de criar suas próprias invenções eletrônicas programáveis. O que você fará com elas dependerá apenas de sua criatividade!

## O que é Raspberry Pi Pico?
O Raspberry Pi Pico é uma maravilha em miniatura, colocando a mesma tecnologia que sustenta desde sistemas de casa inteligente até fábricas industriais na palma da sua mão. Esteja você interessado em aprender sobre a linguagem de programação MicroPython, dando os primeiros passos na computação física, ou deseja construir um projeto de hardware, o Raspberry Pi Pico pode lhe apoiar em cada etapa do caminho.

O Raspberry Pi Pico é conhecido como uma placa de desenvolvimento de microcontrolador, o que significa simplesmente que é uma placa de circuito impresso que abriga um tipo especial de processador projetado para contato com o mundo físico: o microcontrolador. Do tamanho de um pedaço de goma de mascar, o Raspberry Pi Pico possui uma surpreendente quantidade de potência graças ao chip no centro da placa: um microcontrolador RP2040.

O Raspberry Pi Pico não foi projetado para substituir o computador que você tem em casa, que pertence a uma classe diferente de dispositivo conhecido como computador pessoal ou _Personal Computer_ (PC) em inglês. Enquanto você pode usar o seu PC para jogar jogos, escrever histórias e navegar na web, o Raspberry Pi Pico foi projetado para projetos de computação física onde ele controla desde LEDs e botões até sensores, motores e até mesmo outros microcontroladores. 

Ao longo deste curso, você aprenderá tudo sobre o Raspberry Pi Pico, mas as habilidades que você adquirir também se aplicarão a qualquer outra placa de desenvolvimento baseada no microcontrolador RP2040, e até mesmo a outros dispositivos, contanto que sejam compatíveis com a linguagem de programação MicroPython.

## Conhecendo o Raspberry Pi Pico
O Raspberry Pi Pico é um dispositivo muito compacto. Apesar disso, ele inclui uma série de recursos, todos acessíveis pelos pinos ao redor da borda da placa. Se você observar as bordas mais longas, verá seções de cor dourada. Esses são os pinos que fornecem ao microcontrolador RP2040 conexões com o mundo exterior, conhecidos como entrada/saída, ou _Input/Output_ (I/O) em inglês.

![Raspberry Pi Pico visto de cima](images/pico-top.png "Raspberry Pi Pico visto de cima")

O chip no centro do seu Pico é um microcontrolador RP2040. Este é um Circuito Integrado (CI) personalizado, projetado e construído especificamente pelos engenheiros para dar poder computacional ao seu Pico e outros dispositivos baseados em microcontrolador. Se você olhar para ele contra a luz, verá um logotipo da Raspberry Pi gravado na parte superior do chip, juntamente com uma série de letras e números que permitem aos engenheiros rastrear quando e onde o chip foi fabricado.

Na parte superior do seu Pico há uma porta micro USB. Ela fornece energia para o funcionamento do seu Pico e também permite que o Pico se comunique com um computador através da sua porta USB, o que permite carregar seus programas no seu Pico. Se você segurar o seu Pico e olhar para a porta micro USB de frente, verá que ela é mais estreita na parte inferior e mais larga na parte superior. Pegue um cabo micro USB e você verá que o conector tem a mesma forma.

> `Atenção`: O cabo micro USB só se encaixará na porta micro USB do seu Pico de uma maneira. Ao conectá-lo, certifique-se de alinhar os lados estreito e largo da maneira correta ou você pode danificar o seu Pico ao tentar forçar o cabo micro USB na direção errada!

Logo abaixo da porta micro USB há um pequeno botão marcado como BOOTSEL. BOOTSEL é a abreviação de 'seleção de inicialização', que alterna o seu Pico entre dois modos de inicialização quando é ligado pela primeira vez. Você usará o botão de seleção de inicialização mais tarde, à medida que prepara o seu Pico para a programação com MicroPython.

Na parte inferior do seu Pico, há três pequenos pinos dourados com a palavra 'DEBUG' acima deles. Eles são projetados para depuração, ou seja, encontrar erros em programas em execução no Pico, usando uma ferramenta especial chamada debugger. Você não fará esse tipo de depuração de código de programas neste curso, mas pode achá-lo útil à medida que escreve programas maiores e mais complicados.

Vire o seu Pico e você verá que a parte inferior tem escritos rotulando cada um dos pinos com sua função principal. Você verá coisas como 'GP0' e 'GP1', 'GND', 'RUN' e '3V3'. Se você esquecer qual pino é qual, esses rótulos irão te ajudar. Mas você não poderá vê-los quando o Pico estiver inserido em uma placa de prototipagem (_breadboard_). Por isso você pode consultar o diagrama que segue para facilitar a referência sempre que necessário.

![Diagrama dos pinos do Pico](images/pico-pinout.png "Diagrama dos pinos do Pico")

Se você tiver uma placa de prototipagem, insira o seu Raspberry Pi Pico na placa de forma que ele cubra a divisão do meio e a porta micro USB esteja no topo da placa, conforme a figura que segue. Empurre delicadamente o Pico para baixo até que as partes plásticas dos pinos estejam tocando a placa de prototipagem. Isso significa que as partes metálicas dos pinos estão totalmente inseridas e fazendo um bom contato elétrico com a placa de prototipagem.

O pino superior esquerdo, Pino `0`, deve estar na fileira marcada com um `1`, se sua placa de prototipagem estiver numerada. Antes de empurrar o seu Pico para baixo, certifique-se de que os pinos estejam todos devidamente posicionados. Se você dobrar um pino, pode ser difícil endireitá-lo novamente sem quebrá-lo.

![Pico inserido na placa de prototipagem](images/pico-breadboard.png "Pico inserido na placa de prototipagem")

> `Dica`: Insira o Pico com o conector micro USB posicionado para o topo da placa de prototipagem conforme a figura. Isso facilitará a conexão do cabo micro USB posteriormente.

Agora conecte o seu cabo micro USB à porta localizada no lado esquerdo do Pico.

![Conectando cabo micro usb ao Pico](images/micro-usb-pico.png "Conectando cabo micro usb ao Pico")

> `Atenção`: Seja gentil ao conectar o cabo micro USB ao seu Pico. O conector do Pico é frágil e pode danificar facilmente. Após fixar o cabo, evite retirá-lo com frequência.

## Programando com MicroPython
Desde o seu lançamento em 1991, a linguagem de programação Python, nomeada após a famosa série de televisão Monty Python, em vez da serpente, cresceu para se tornar uma das mais populares no mundo. Sua popularidade, no entanto, não significa que não haja melhorias que possam ser feitas especialmente se você estiver trabalhando com um microcontrolador. 

A linguagem de programação Python foi desenvolvida para sistemas de computador como desktops, laptops e servidores. Placas de microcontrolador como o Raspberry Pi Pico são menores, mais simples e têm consideravelmente menos memória, o que significa que não conseguem executar a mesma linguagem Python que seus equivalentes maiores.

É aqui que o MicroPython entra em cena. Originalmente desenvolvido por Damien George e lançado pela primeira vez em 2014, o MicroPython é uma linguagem de programação compatível com Python desenvolvida especificamente para microcontroladores. Ele inclui muitas das características do Python convencional, enquanto adiciona uma variedade de novas funcionalidades projetadas para aproveitar as facilidades disponíveis no Raspberry Pi Pico e em outras placas de microcontrolador. Se você já programou em Python antes, encontrará o MicroPython imediatamente familiar. Se não, não se preocupe: é uma linguagem fácil de aprender!

## Thonny Python IDE
O Thonny é um ambiente de desenvolvimento integrado (IDE) para a linguagem de programação Python. Ele é projetado especialmente para iniciantes e estudantes de programação. O Thonny oferece uma interface de usuário simples e intuitiva, o que o torna mais fácil de usar para aqueles que estão aprendendo a programar em Python.

Algumas das características do Thonny incluem:
* `Editor de código`: possui um editor de código com destaque de sintaxe, sugestões de código e outras funcionalidades para facilitar a escrita de código Python.
* `Shell integrado`: possui um shell Python integrado, permitindo que os usuários testem rapidamente pequenos trechos de código sem a necessidade de criar um arquivo Python separado.
* `Depurador simples`: oferece funcionalidades de depuração para ajudar a identificar e corrigir erros no código.
* `Explorador de variáveis`: permite visualizar o estado das variáveis durante a execução do programa.
* `Gerenciador de pacotes integrado`: Facilita a instalação e gerenciamento de bibliotecas e pacotes Python.
* `Suporte a placas microcontroladoras`: Thonny é compatível com microcontroladores como o Raspberry Pi Pico, o que facilita a programação de dispositivos embarcados.

No geral, o Thonny é uma escolha popular para iniciantes em Python devido à sua interface amigável e às ferramentas úteis que oferece para facilitar o aprendizado da linguagem de programação e de desenvolvimento de sistemas computação física.

A seguir você irá instalar o Thonny, irá se conectar ao seu Raspberry Pi Pico e também executar um código Python simples usando o Shell.

## Instalando o Thonny Python IDE
Você pode instalar a versão mais recente do Thonny IDE no Windows, macOS e Linux, ou seja, o Thonny está presente em todas as plataformas. Em um navegador da web, acesse [thonny.org](https://thonny.org/). No canto superior direito da janela do navegador, você verá os links de download para Windows e macOS, além das instruções para Linux. Siga as instruções apresentadas de acordo com o seu sistema operacional para instalar o Thonny.

![Links com instruções de instalação do Thonny](images/links-thonny.png "Links com instruções de instalação do Thonny")

O Thonny Python IDE vem pré-instalado com o suporte para MicroPython. Portanto, quando você instalar o Thonny, já terá a capacidade de programar em MicroPython sem a necessidade de instalar nenhum pacote adicional. 

Agora abra o Thonny a partir do seu iniciador de aplicativos e você será apresentado à sua tela principal. 

![Tela principal do Thonny](images/thonny-main-screen.png "Tela principal do Thonny")

Você também pode usar o Thonny para escrever código Python padrão. Digite o seguinte na janela principal e depois clique no botão `Run`. 

```Python
print('Hello World!')
```

Não é necessário entender esse código agora. Utilizamos esse procedimento apenas para testar o seu ambiente e garantir que a instalação do Thonny tenha sido bem sucedida. Caso não obtenha o resultado como na figura que segue, repita os procedimentos anteriores.

![Hello World no Thonny](images/thonny-hello-world.png "Hello World no Thonny")

O botão `Run` está localizado na barra de ferramentas do Thonny, logo abaixo da barra de menus principal e permite executar um programa. 

![Barra de ferramentas do Thonny](images/thonny-tool-bar.png "Barra de ferramentas do Thonny")

Nessa barra também se encontra o botão `Stop` que é usado para encerrar a execução de um programa. Caso precise, posicione o seu mouse sobre um botão da barra de ferramentas e aguarde parado por alguns segundos. Uma pequena caixa de texto aparecerá com a descrição daquela função.  

## Adicione o firmware MicroPython
Caso esteja ligando pela primeira vez o seu Raspberry Pi Pico, será necessário adicionar o firmware do MicroPython nele.

Primeiramente confirme que cabo micro USB está conectado na porta micro USB do seu Pico. Agora encontre o botão `BOOTSEL` no seu Raspberry Pi Pico.

![Localização do botão BOOTSEL](images/pico-bootsel.png "Localização do botão BOOTSEL")

Pressione o botão `BOOTSEL` e mantenha-o pressionado enquanto conecta a outra ponta do cabo micro USB ao seu computador. Uma imagem de um Raspberry Pi é mostrada a seguir, mas o mesmo se aplica a qualquer outro computador.

![Cabo USB sendo conectado ao seu computador](images/pico-usb-connection.png "Cabo USB sendo conectado ao seu computador")

Após conectar o cabo micro USB ao seu computador, solte o botão `BOOTSEL`. Isso coloca o seu Raspberry Pi Pico no modo de dispositivo de armazenamento em massa USB.

> `Atenção`: Fique atento à sequência de instruções acima. O botão `BOOTSEL` deve estar pressionado enquanto se conecta o cabo micro USB ao computador, e logo em seguida liberado.

> `Atenção`: É importante destacar a diferença entre o Raspberry Pi e o Raspberry Pi Pico na imagem anterior. Enquanto o Raspberry Pi é um computador completo com capacidade de desktop, o Raspberry Pi Pico é mais como um cérebro muito poderoso, mas sem a mesma capacidade de realizar tarefas de desktop como navegação na internet ou edição de documentos.

Na parte inferior direita da janela do Thonny, você verá a versão do Python que está atualmente em uso.

![Localização da versão do Python no Thonny](images/thonny-path.png "Localização da versão do Python no Thonny")

Clique na versão do Python e escolha 'MicroPython (Raspberry Pi Pico)'.

![Seleção da linguagem MicroPython](images/thonny-path-firmware.png "Seleção da linguagem MicroPython")

Se você não vê esta opção, verifique se você conectou o seu Raspberry Pi Pico corretamente. Se tudo correr bem, uma caixa de diálogo irá aparecer para instalar a versão mais recente do firmware MicroPython no seu Raspberry Pi Pico.

![Tela de instalação de firmware](images/install-firmware-screen.png "Tela de instalação de firmware")

Clique no botão `Install` para gravar o firmware no seu Raspberry Pi Pico.
Aguarde a instalação ser concluída e clique em `Close`.

> `Dica`: Você não precisa atualizar o firmware toda vez que usar o seu Raspberry Pi Pico. Da próxima vez, você pode simplesmente conectá-lo ao seu computador sem pressionar o botão `BOOTSEL`.

## Usando o Shell
> `Importante`: Antes de continuar, certifique-se de que o seu Raspberry Pi Pico está conectado ao seu computador e que você selecionou o interpretador 'MicroPython (Raspberry Pi Pico)'.

Com o cabo micro USB conectado ao seu computador o Thonny é capaz de se comunicar com o seu Raspberry Pi Pico usando o REPL (loop de leitura-avaliação-escrita ou _Read–Eval–Print Loop_ em inglês), o que permite que você digite código Python no painel do Shell e veja a saída imediatamente. Dessa forma você pode digitar comandos diretamente no painel do Shell e eles serão executados no seu Raspberry Pi Pico de forma interativa.

No painel do Shell, localizado na parte inferior do editor Thonny, digite o seguinte comando. 

```Python
print('Hello World!')
```

Pressione a tecla `Enter` e você verá a saída.

![Thonny shell após execução de Hello World](images/thonny-shell-hellow.png "Thonny shell após execução de Hello World")

A função `print` em Python exibe informações na saída padrão, geralmente na tela do seu computador. Ele é usado para mostrar mensagens, resultados de cálculos, variáveis e outros tipos de dados. Nesse caso a função apresentou a string 'Hello World' no painel do Shell.

Uma string em Python é uma sequência de caracteres, ou seja, um conjunto ordenado de caracteres alfanuméricos, símbolos ou espaços em branco. As strings são usadas para representar texto em programas Python. Em Python as strings devem estar entre aspas simples `'`, ou aspas entre aspas duplas `"`. Dessa forma ambas as strings que seguem são válidas.

```Python
'Hello World.'
"Hello World."
```

O importante é ser consistente: se você iniciou uma string com aspas simples, feche-a com aspas simples. Se iniciou com aspas duplas, feche-a com aspas duplas.

As funções em Python, assim como na maioria das linguagens de programação, utilizam um par de parenteses `()` para indicar onde os argumentos devem ser colocados.  Por isso a string 'Hello World!' foi colocada dentro dos parênteses da função `print`.

O MicroPython adiciona bibliotecas específicas de hardware, como `machine`, que você pode usar para programar o seu Raspberry Pi Pico. Vamos criar um objeto `machine.Pin` para corresponder ao LED embarcado, que pode ser acessado usando o pino `25`.

Se você definir o valor do LED como `1`, ele se acende.

Digite o seguinte código, e certifique-se de pressionar `Enter` após cada linha.

```Python
from machine import Pin
led = Pin(25, Pin.OUT)
led.value(1)
```

Você deverá ver o LED embarcado se acender. Confirme isso localizando o LED embarcado em seu Pico.
'Embarcado' neste contexto significa que o LED faz parte do próprio Raspberry Pi Pico. É como aquela luzinha que já vem junto com a sua televisão e indica se ela está ligada. Portanto, o 'LED embarcado do Raspberry Pi Pico' se refere ao LED que está diretamente conectado e vem junto com o próprio Raspberry Pi Pico.

Agora digite o seguinte código para definir o valor como `0` e desligar o LED embarcado.

```Python
led.value(0)
```

Uma dica valiosa para tornar os códigos mais intuitivos é substituir `led.value(1)` por `led.high()` nos exemplos anteriores. Da mesma forma, `led.value(0)` pode ser substituído por `led.low()`. Essas alterações podem tornar os comandos mais claros e fáceis de compreender. A escolha é sua!

Ligue e desligue o LED quantas vezes desejar.

> `Dica`: Você pode usar a seta para cima no teclado para acessar rapidamente linhas de código anteriores.

## Faça o LED embarcado piscar
Apesar de ser vantajoso utilizar o painel de Shell para realizar testes de código de forma rápida e interativa, se você deseja escrever um programa mais longo é melhor salvá-lo em um arquivo para poder reutilizá-lo mesmo após reiniciar seu Pico.

O Thonny pode salvar e executar programas MicroPython diretamente no seu Raspberry Pi Pico. Para testar isso você irá criar um programa em MicroPython para fazer o LED embarcado alternar entre ligado e desligado.

Clique no painel principal do editor do Thonny localizado na parte superior da tela. Digite o seguinte código para alternar o LED.

```Python
from machine import Pin
led = Pin(25, Pin.OUT)

led.toggle()
```

A primeira linha de código importa uma biblioteca do MicroPython chamada `machine` que contém funções para interagir com hardware. Mais especificamente, ela está importando a função `Pin`, que permite controlar os pinos do Raspberry Pi Pico.

Na segunda linha é criada uma variável chamada `led`. Esta variável é configurada para controlar o pino `25` do Raspberry Pi Pico, que está conectado ao LED embarcado da placa. A segunda parte `Pin.OUT` significa que este pino será usado para enviar um sinal de saída (como acender ou apagar um LED).

A última linha está dizendo para o LED trocar de estado. Se o LED estiver aceso, ele será apagado, e vice-versa.

![Alternando o LED embarcado entre ligado e desligado](images/thonny-led-toggle.png "Alternando o LED embarcado entre ligado e desligado")

Clique em `File -> Save as...` para salvar seu programa. O Thonny perguntará se você deseja salvar o arquivo em seu computador 'This computer' ou em seu Raspberry Pi Pico. Escolha 'Raspberry Pi Pico'. 

![Salvando o arquivo no Pico](images/this-computer-or-pico.png "Salvando o arquivo no Pico")

Digite 'blink.py' como o nome do arquivo.

> `Dica`: Você precisa incluir a extensão `.py` para que o Thonny reconheça o arquivo como um arquivo MicroPython.

Agora clique no botão `Run` para executar seu código. Você deverá ver o LED embarcado alternar entre ligado e desligado a cada vez que clicar no botão `Run`.

Você pode usar a biblioteca `Timer` para configurar um temporizador que executa uma função em intervalos regulares.

Atualize seu código para que pareça com isso.

```Python
from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
```

A primeira linha agora importa também a biblioteca `Timer` que permite configurar e gerenciar temporizadores.

A terceira linha cria um objeto chamado `timer`. Este objeto será usado para configurar um temporizador que irá chamar uma função em intervalos regulares.

Na quarta linha `def blink(timer)`: é uma função. Uma função é um conjunto de instruções que podem ser usadas repetidamente. No caso, esta função é chamada de `blink` e ela recebe um parâmetro chamado `timer`. `def` é uma palavra-chave importante em MicroPython que é usada para definir funções. A sintaxe de MicroPython exige que se coloque dois pontos `:` no final da linha de declaração da função. Funções são parte fundamental da programação, permitindo a organização e reutilização de código.

Uma parte importante aqui é a indentação. A indentação refere-se aos espaços ou tabulações que são usados no início das linhas para organizar o código. No MicroPython, a indentação é muito importante e é usada para indicar quais instruções estão dentro de um bloco de código.

No exemplo dado, a linha `led.toggle()` está indentada. Isso significa que ela faz parte do bloco de código da função `blink`. Ou seja, quando a função `blink` é chamada, o programa executa `led.toggle()` como parte dessa função. Se `led.toggle()` não estivesse indentada, o MicroPython não entenderia que ela faz parte da função `blink`. A indentação é como uma forma de dizer ao MicroPython quais partes do código pertencem a uma função.

A última linha inicializa o temporizador que criamos anteriormente. Ele é configurado para uma frequência de 2,5 Hz (ou seja, a função `blink` será chamada a cada 0,4 segundos), com o modo de operação `Timer.PERIODIC` (significando que o temporizador irá chamar a função de forma repetida). O `callback=blink` indica que a função a ser chamada é a função `blink` definida anteriormente.

O conceito de 'frequência', em termos simples, se refere a quantas vezes algo acontece em um determinado intervalo de tempo. No contexto do temporizador, isso significa quantas vezes ele executa uma ação específica dentro do intervalo de 1 segundo. Neste caso, a frequência é 2,5 vezes por segundo, o que significa que a função `blink` será chamada 2,5 vezes a cada segundo. Se você definisse a frequência como 0,5, o LED piscaria apenas a cada dois segundos, o que seria mais devagar.

Em códigos MicroPython, lembre-se de utilizar o padrão norte-americano para valores decimais. Nele, o separador decimal é o ponto `.`, e não a vírgula `,`. Por exemplo, o número `0,5` deve ser inserido como `0.5` no código.

Clique em `Run` e o seu programa fará o LED piscar até que você clique no botão `Stop`. Lembre que os botões `Run` e `Stop` estão localizados na barra de ferramentas do Thonny, logo abaixo da linha de menus. 

## Descobrindo os Segredos da Eletricidade

Bem-vindo a um mundo emocionante onde a eletricidade se torna mágica! A eletricidade é uma forma de energia que pode ser controlada e utilizada para fazer coisas incríveis. Ela é composta por minúsculas partículas chamadas elétrons, que agem como mensageiros de energia.

Esses elétrons percorrem caminhos invisíveis chamados circuitos. Imagine-os como estradas especiais, onde a energia viaja para alimentar nossos projetos. Em um circuito, a eletricidade sempre flui de um ponto de tensão alta para um ponto de tensão baixa.

Um LED é como uma pequena lâmpada que emite luz quando a eletricidade passa por ele. Quando escrevemos `pin.high()`, estamos dizendo ao Raspberry Pi Pico para configurar o pino para ter um nível de tensão alta, geralmente 3,3V, o que permite a passagem de corrente elétrica (elétrons), passando pelo LED, e retornando para o 'terra' (ou _ground_ em inglês ou 'GND') do Raspberry Pi Pico.

É fundamental garantir que o circuito esteja completamente conectado, com todos os componentes eletricamente unidos, para permitir o fluxo da corrente elétrica. É aqui que uma placa de prototipagem e fios de conexão podem ajudar, como veremos adiante.

Por outro lado, `pin.low()` faria o oposto, configurando o pino para ter um nível de tensão baixo, o que efetivamente corta a energia no pino e não permite que a corrente elétrica flua. 

Essa jornada da eletricidade pelo LED é o que faz com que ele brilhe. Um LED é um componente eletrônico que emite luz quando uma corrente elétrica o atravessa. Ele é construído a partir de materiais que têm propriedades especiais para esse efeito. A cor da luz emitida pelo LED depende do tipo de material utilizado. Diferentes materiais resultam em cores variadas, como vermelho, verde, azul, entre outras.

Com essas habilidades, podemos acender luzes, mover motores, e até mesmo criar projetos mais complexos. Agora que você conhece os fundamentos da eletricidade e circuitos, está pronto para dar vida aos seus projetos com MicroPython! 

## Usando uma Placa de Prototipagem
Os projetos a seguir serão muito mais fáceis de concluir se você estiver usando uma placa de prototipagem para segurar os componentes e realizar as conexões elétricas.

Uma placa de prototipagem está coberta com pequenos furos ou orifícios espaçados com 2,54 mm de distância. Debaixo desses orifícios, existem tiras de metal que funcionam como os fios de conexão, identificadas em verde na figura que segue. Estes percorrem em fileiras pela placa, com a maioria das placas tendo uma abertura no meio para dividi-las em dois lados.

![Placa de prototipagem](images/breadboard-internal-wiring.png "Placa de prototipagem")

Muitas placas de prototipagem têm letras na parte superior e números nas laterais. Isso permite que você encontre um orifício específico: A1 é o canto superior esquerdo, B1 é o orifício imediatamente à direita, enquanto B2 é um orifício abaixo dali. A1 está conectado a B1 pelas tiras de metal ocultas, mas nenhum orifício marcado com um 1 está conectado a qualquer orifício marcado com um 2, a menos que você adicione um fio de conexão por conta própria. 

Placas de prototipagem maiores também têm fileiras de orifícios nas laterais, geralmente marcadas com listras vermelhas e pretas ou vermelhas e azuis. Estas são as trilhas de energia, e são projetadas para facilitar a conexão dos fios: você pode conectar um único fio de um dos pinos de terra do seu Pico a uma das trilhas de energia, que são normalmente marcadas com uma listra azul ou preta e um símbolo de menos, para fornecer um terra comum para muitos componentes na placa. Você pode fazer o mesmo se o seu circuito precisar de energia de 3,3 V ou 5 V utilizando a trilha com listra vermelha. Todos os orifícios de uma mesma trilha estão conectados eletricamente. 

Inserir componentes eletrônicos a uma placa de prototipagem é simples: alinhe seus terminais (as partes metálicas salientes) com os orifícios e empurre suavemente até que o componente esteja no lugar. Nunca tente inserir mais de um terminal de componente ou fio de conexão em um mesmo orifício na placa. 

> `Importante`: Os orifícios estão conectados em fileiras, exceto pela divisão no meio, então o terminal de componente inserido em A1 está eletricamente conectado a qualquer coisa que você insira em B1, C1, D1 e E1, e não conectado aos orifícios F1, G1, H1, I1 ou J1. 

## Resistores
Os resistores são usados em circuitos para reduzir o fluxo de corrente elétrica. Isso os torna úteis na proteção de certos componentes que podem se danificar se uma corrente muito alta passar por eles. Também são úteis para garantir que uma voltagem muito específica seja fornecida a outro componente.

![Array de Resistores Eletrônicos de Pinos Axiais](images/resistors.jpg "Array de Resistores Eletrônicos de Pinos Axiais")

O valor de um resistor é medido em `ohms` e utiliza o símbolo `Ω`.

Você pode determinar o valor da resistência de um resistor pela cor das faixas nele presentes. A maioria dos resistores possui 4 faixas, mas resistores de 5 e 6 faixas também estão disponíveis.

Em um resistor de 4 faixas, a primeira cor indica o primeiro dígito do valor, a segunda faixa indica o segundo dígito do valor, e a terceira faixa indica o que multiplicar pelos dois primeiros dígitos (ou quantos zeros adicionar no final). A quarta faixa indicará a precisão do valor do resistor calculada como uma porcentagem.

![Código de cores em resistores](images/color-code-resistors.png "Código de cores em resistores")

Por exemplo, com as faixas, é possível calcular o valor em ohms destes resistores da seguinte forma:

![Resistor mostrando faixas de vermelho, vermelho, marrom](images/220-resistor.png "Resistor mostrando faixas de vermelho, vermelho, marrom")

Vermelho Vermelho Marrom = 2 2 1 = 2 2 x 10 = 220Ω.

![Resistor mostrando faixas de violeta, verde, preto](images/75-resistor.png "Resistor mostrando faixas de violeta, verde, preto")

Violeta Verde Preto = 7 5 1 = 7 5 x 1 = 75Ω.

Ao usar LEDs com um Raspberry Pi Pico, você deve utilizar um resistor de cerca de 100Ω (ohms). Qualquer resistor entre 75Ω e 220Ω funcionará.

## LEDs
Diodos Emissores de Luz, ou _Light Emitting Diodes_ (LED) em inglês, emitem luz quando uma corrente elétrica passa por eles. Existem LEDs em muitas cores diferentes.

![3 LEDs nas cores vermelho, verde e azul](images/3-leds-rgb.jpg "3 LEDs nas cores vermelho, verde e azul")

Normalmente, um LED precisará de um resistor para ser usado. Isso ocorre porque uma corrente elétrica muito alta pode fazer com que um LED queime ou até mesmo exploda. 

Para obter o brilho máximo de um LED, você precisa encontrar o resistor correto para usar. Quando você compra um LED, pode consultar a sua especificação técnica, conhecido como _datasheet_ para encontrar sua tensão direta _forward voltage_, e a sua corrente direta _forward current_.

A tensão é medida em `Volts`, cujo símbolo é `V`. E a corrente é medida em `Amperes`, cujo símbolo é `A`.

Por exemplo, caso o _datasheet_ informe os seguintes valores para seu LED:
* _forward voltage_ = 2,1 V (2,1 volts)
* _forward current_ = 25 mA (25 miliamperes)

E sabendo que a tensão em volts (V) de fornecimento do Raspberry Pi Pico é de `3,3 V`, você pode calcular o valor do resistor necessário como segue.

* Resistência Necessária = ( 3,3 V - _forward voltage_ ) / _forward current_

A corrente direta _forward current_ deve ser fornecida na unidade Amperes. Portanto divida o valor do _datasheet_ para _forward current_ por `1000` nesse caso antes de substituir na fórmula anterior.

Por exemplo, para os dados do LED acima, é necessário um resistor de pelo menos 48 Ω, conforme o cálculo que segue:

* Resistência Necessária = ( 3,3 V - 2,1 V ) / 0,025 A = 48 Ω

Seu resistor pode ser conectado a qualquer um dos pinos do seu LED, e depois ao seu Raspberry Pi Pico. Entretanto o LED só acenderá quando a eletricidade passar por ele na direção correta, do pino mais longo (ânodo) para o pino mais curto (cátodo).

## Fios de conexão com pinos e soquetes
Os fios de conexão, também conhecidos como _jumpers_, são usados para conduzir a corrente elétrica entre os componentes eletrônicos. Eles são utilizados em projetos de prototipagem porque permitem que você conecte e desconecte os componentes sem a necessidade de soldagem (criando conexões mais permanentes ao fundir o metal).

Existem três tipos diferentes de fios de conexão:
* soquete-soquete, ou fêmea-fêmea (F-F)
* pino-soquete, ou macho-fêmea (M-F)
* pino-pino, ou macho-macho (M-M)

Cada tipo é identificado pelo que está colocado em cada extremidade do fio.

Uma extremidade de pino possui um pequeno pedaço de metal saindo da extremidade de plástico preto. Isso pode ser inserido dentro de uma extremidade de soquete ou em uma placa de prototipagem.

![A extremidade de pino de um fio de conexão](images/pin.png "A extremidade de pino de um fio de conexão")

A extremidade de soquete parece uma pequena peça de plástico preto. Ela tem um orifício no interior que pode receber uma extremidade de pino.

![A extremidade de soquete de um fio de conexão](images/socket.png "A extremidade de soquete de um fio de conexão")

## Piscando um LED externo
Agora que você conhece o básico, pode controlar um LED externo com o seu Raspberry Pi Pico e também fazê-lo ler a entrada de um botão externo.

Use um resistor entre 50 e 330 ohms, um LED vermelho e um par de fios de conexão M-M para conectar o seu Raspberry Pi Pico conforme mostrado na imagem abaixo.

![LED e resistor conectados ao Pico](images/single_LED.png "LED e resistor conectados ao Pico")

Neste exemplo, o LED está conectado ao pino 15. Se você usar um pino diferente, lembre-se de procurar o número no diagrama de pinos do Raspberry Pi Pico.

Use o mesmo código que você usou para piscar o LED embarcado, mas mude o número do pino para `15`.

```python
from machine import Pin, Timer
led = Pin(15, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
```

Execute o seu programa e o LED deverá começar a piscar. Se não estiver funcionando, verifique a sua conexão para ter certeza de que o LED está conectado corretamente.

Em seguida, vamos tentar controlar o LED usando um botão. Adicione um botão ao seu circuito conforme mostrado no diagrama abaixo.

![LED e botão em uma placa de prototipagem](images/button_and_LED.png "LED e botão em uma placa de prototipagem")

Um pino do botão está conectado ao pino `14` do seu Raspberry Pi Pico e o outro pino do botão está conectado ao pino `3.3V` do seu Raspberry Pi Pico. Ao configurar o pino do seu Pico, você precisa informar ao MicroPython que ele é um pino de entrada e precisa ser puxado para baixo, ou _pulled down_ em inglês, o que significa que o pino `14` do Pico lerá o valor lógico `0 zero` caso o botão não esteja pressionado, e o valor lógico `1 um` caso o botão esteja pressionado. Existem palavras-chave em MicroPython para esses valores lógicos: `True` é o mesmo que `1` e `False` é o mesmo que `0'.

Crie um novo arquivo e adicione este código.

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

Execute o seu código e então, quando você pressionar o botão, o LED deverá acender ou apagar. Se você segurar o botão pressionado, ele irá piscar.

Entenda a explicação do código linha por linha:

1. `from machine import Pin`: Esta linha importa uma biblioteca que permite ao Raspberry Pi Pico controlar os seus pinos. 

2. `import time`: Aqui é importada a biblioteca que permite lidar com o temporizadores, como fazer o programa esperar por um tempo específico sem fazer nada.

3. `led = Pin(15, Pin.OUT)`: Aqui é criada uma variável chamada `led` (que poderia ser qualquer outro nome) e dizendo que ela está conectada ao pino 15 do seu Raspberry Pi Pico. Além disso, está configurando este pino como uma saída `Pin.OUT`. Isso significa que esse pino pode enviar corrente elétrica para acender um LED conectado a ele através de um fio de conexão (jumper).

4. `button = Pin(14, Pin.IN, Pin.PULL_DOWN)`: Da mesma forma, aqui é criada uma variável chamada `button` conectada ao pino 14 do seu Raspberry Pi Pico. O pino é configurando como uma entrada `Pin.IN`. Isso significa que o pino pode 'escutar' se existe eletricidade passando por ele ou não. O `Pin.PULL_DOWN` significa que há uma resistência especial ligada ao pino que ajuda a manter o valor do pino como `0 zero` quando não há corrente elétrica.

5. `while True:`: Esta linha inicia um loop que vai continuar para sempre, a menos que algo o pare. É como dizer 'faça isso para sempre'.

6. `if button.value():`: Aqui se verifica se o botão está sendo pressionado. `button.value()` retorna `True` se o botão estiver pressionado e `False` se não estiver.

7. `led.toggle()`: Se o botão estiver pressionado, esta linha muda o estado do LED. Se o LED estiver aceso, ele é apagado, e vice-versa.

8. `time.sleep(0.5)`: Esta linha faz o programa esperar por meio segundo (0,5 segundos) antes de continuar. É como um pequeno intervalo de tempo para que possamos ver o LED piscar.

O código geral faz com que o LED pisque cada vez que o botão é pressionado. Se o botão for mantido pressionado, o LED continuará piscando a cada meio segundo até que o botão seja solto.

Aqui cabem algumas explicações adicionais:

* Note a utilização da palavra-chave de MicroPython, ou _keyword_ em inglês, `while`. Essa construção repete o bloco de código que estiver 'dentro' dela enquanto a condição lógica passada a ela for avaliada como verdadeira, ou `True`. Como nesse caso foi colocado o valor `True` fixo no código, o bloco de código será repetido para sempre. Para colocar uma ou mais linhas de código 'dentro' do `while`, colocam-se 4 espaços no início de cada uma das linhas. Esses 4 espaços são conhecidos como `indentação`. Ou seja, as linhas são 'indentadas' e com isso passam a ser 'comandadas' pela ação do `while`.
* Utiliza-se aqui também a palavra-chave de MicroPython `if`. Essa construção executa o bloco de código indentado caso a condição lógica passada a ela seja avaliada como verdadeira, ou `True`. Caso contrário o bloco indentado não será executado.


