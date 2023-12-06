## Capítulo 3: Preparação do ambiente de desenvolvimento

Prepare-se para dar um mergulho empolgante na preparação do ambiente de desenvolvimento com o incrível Thonny Python IDE! Neste capítulo, vamos explorar passo a passo a configuração do seu ambiente para programar em Python e trabalhar com o Raspberry Pi Pico.

O Thonny é uma ferramenta incrível para quem está começando a aprender MicroPython, oferecendo uma interface intuitiva e diversas funcionalidades que facilitam o desenvolvimento e a depuração de código. Com um editor de código intuitivo, shell integrado e suporte para placas microcontroladoras como o Raspberry Pi Pico, o Thonny é um aliado poderoso para quem está se aventurando no mundo da computação física.

Neste capítulo, vamos guiar você por todo o processo, desde a instalação do Thonny em diferentes sistemas operacionais até a configuração do ambiente para programar no Raspberry Pi Pico. Prepare-se para instalar o Thonny, conectar-se ao seu Raspberry Pi Pico e executar seu primeiro código Python diretamente do Shell!

### Thonny Python IDE

O Thonny é um ambiente de desenvolvimento integrado (IDE, Integrated Development Environment em inglês) para a linguagem de programação Python. Ele é projetado especialmente para iniciantes e estudantes de programação. O Thonny oferece uma interface de usuário simples e intuitiva, o que o torna mais fácil de usar para aqueles que estão aprendendo a programar em Python.

Algumas das características do Thonny incluem:

- **Editor de código**: possui um editor de código com destaque de sintaxe, sugestões de código e outras funcionalidades para facilitar a escrita de código Python.

- **Shell integrado**: possui um shell Python integrado, permitindo que os usuários testem rapidamente pequenos trechos de código sem a necessidade de criar um arquivo Python separado.

- **Depurador simples**: oferece funcionalidades de depuração para ajudar a identificar e corrigir erros no código.

- **Explorador de variáveis**: permite visualizar o estado das variáveis durante a execução do programa.

- **Gerenciador de pacotes integrado**: Facilita a instalação e gerenciamento de bibliotecas e pacotes Python.

- **Suporte a placas microcontroladoras**: Thonny é compatível com microcontroladores como o Raspberry Pi Pico, o que facilita a programação de dispositivos embarcados.

No geral, o Thonny é uma escolha popular para iniciantes em Python devido à sua interface amigável e às ferramentas úteis que oferece para facilitar o aprendizado da linguagem de programação e de desenvolvimento de sistemas computação física.

A seguir você irá instalar o Thonny, irá se conectar ao seu Raspberry Pi Pico e também executar um código Python simples usando o Shell.

### Instalando o Thonny Python IDE

Você pode instalar a versão mais recente do Thonny IDE no Windows, macOS ou Linux, ou seja, o Thonny está presente em todas as plataformas. Em um navegador da web, acesse [thonny.org](https://thonny.org/). No canto superior direito da janela do navegador, você verá os links de download para **Windows** e **macOS**, além das instruções para **Linux**. Siga as instruções apresentadas de acordo com o seu sistema operacional para instalar o Thonny.

![Links com instruções de instalação do Thonny](/images/links-thonny.png "Links com instruções de instalação do Thonny")

O Thonny Python IDE vem pré-instalado com o suporte para MicroPython. Portanto, quando você instalar o Thonny, já terá a capacidade de programar em MicroPython sem a necessidade de instalar nenhum pacote adicional. 

Agora abra o Thonny a partir do seu iniciador de aplicativos e você será apresentado à sua tela principal. 

![Tela principal do Thonny](/images/thonny-main-screen.png "Tela principal do Thonny")

Você também pode usar o Thonny para escrever código Python padrão. Digite o seguinte na janela principal e depois clique no botão `Run`. 

```Python
print('Hello World em Python!')
```

Não é necessário entender esse código agora. Utilizamos esse procedimento apenas para testar o seu ambiente e garantir que a instalação do Thonny tenha sido bem sucedida. Caso não obtenha o resultado como na figura que segue, repita os procedimentos anteriores.

![Hello World no Thonny](/images/thonny-hello-world.png "Hello World no Thonny")

O botão `Run` está localizado na barra de ferramentas do Thonny, logo abaixo da barra de menus principal e permite executar um programa. 

![Barra de ferramentas do Thonny](/images/thonny-tool-bar.png "Barra de ferramentas do Thonny")

Nessa barra também se encontra o botão `Stop` que é usado para encerrar a execução de um programa. Caso precise, posicione o seu mouse sobre um botão da barra de ferramentas e aguarde parado por alguns segundos. Uma pequena caixa de texto aparecerá com a descrição daquela função.  

### Inserindo o Pico na placa de prototipagem

Se você tiver uma placa de prototipagem, insira o seu Raspberry Pi Pico na placa de forma que ele cubra a divisão do meio e a porta micro USB esteja no topo da placa, conforme a figura que segue. Empurre delicadamente o Pico para baixo até que as partes plásticas dos pinos estejam tocando a placa de prototipagem. Isso significa que as partes metálicas dos pinos estão totalmente inseridas e fazendo um bom contato elétrico com a placa de prototipagem.

O pino superior esquerdo, `GP0`, deve estar na fileira marcada com um 1, se sua placa de prototipagem estiver numerada (algumas placas iniciam pelo valor 0). Antes de empurrar o seu Pico para baixo, certifique-se de que os pinos estejam todos devidamente posicionados. Se você dobrar um pino, pode ser difícil endireitá-lo novamente sem quebrá-lo.

![Pico inserido na placa de prototipagem](/images/pico-breadboard.png "Pico inserido na placa de prototipagem")

Insira o Pico com o conector micro USB posicionado para o topo da placa de prototipagem conforme a figura. Isso facilitará a conexão do cabo micro USB posteriormente.

Agora conecte o seu cabo micro USB à porta localizada no lado esquerdo do Pico.

![Conectando cabo micro usb ao Pico](/images/micro-usb-pico.png "Conectando cabo micro usb ao Pico")

> **`Atenção`**: Seja gentil ao conectar o cabo micro USB ao seu Pico. O conector do Pico é frágil e pode danificar facilmente. Após fixar o cabo, evite retirá-lo com frequência.

### Adicione o firmware MicroPython

Caso esteja ligando pela primeira vez o seu Raspberry Pi Pico, será necessário adicionar o firmware do MicroPython nele.

Primeiramente confirme que cabo micro USB está conectado na porta micro USB do seu Pico. Agora encontre o botão `BOOTSEL` no seu Raspberry Pi Pico.

![Localização do botão BOOTSEL](/images/pico-bootsel.png "Localização do botão BOOTSEL")

Pressione o botão `BOOTSEL` e mantenha-o pressionado enquanto conecta a outra ponta do cabo micro USB ao seu computador. Uma imagem de um Raspberry Pi é mostrada a seguir, mas o mesmo se aplica a qualquer outro computador.

![Cabo USB sendo conectado ao seu computador](/images/pico-usb-connection.png "Cabo USB sendo conectado ao seu computador")

Após conectar o cabo micro USB ao seu computador, solte o botão `BOOTSEL`. Isso coloca o seu Raspberry Pi Pico no "modo de dispositivo de armazenamento em massa USB".

> **`Atenção`**: Fique atento à sequência de instruções acima. O botão `BOOTSEL` deve estar pressionado enquanto se conecta o cabo micro USB ao computador, e logo em seguida liberado.

Na parte inferior direita da janela do Thonny, você verá a versão do Python que está atualmente em uso.

![Localização da versão do Python no Thonny](/images/thonny-path.png "Localização da versão do Python no Thonny")

Clique na versão do Python e escolha 'MicroPython (Raspberry Pi Pico)'.

![Seleção da linguagem MicroPython](/images/thonny-path-firmware.png "Seleção da linguagem MicroPython")

Se você não vê esta opção, verifique se você conectou o seu Raspberry Pi Pico corretamente. Se tudo correr bem, uma caixa de diálogo irá aparecer para instalar a versão mais recente do firmware MicroPython no seu Raspberry Pi Pico.

![Tela de instalação de firmware](/images/install-firmware-screen.png "Tela de instalação de firmware")

Clique no botão `Install` para gravar o firmware no seu Raspberry Pi Pico.
Aguarde a instalação ser concluída e clique em `Close`.

> **`Atenção`**: Você não precisa atualizar o firmware toda vez que usar o seu Raspberry Pi Pico. Da próxima vez, você pode simplesmente conectá-lo ao seu computador sem pressionar o botão `BOOTSEL`.

# Conclusão

Parabéns por concluir a preparação do ambiente de desenvolvimento com sucesso! Durante este capítulo, você aprendeu a instalar o Thonny Python IDE em seu sistema operacional, explorou suas funcionalidades e até mesmo executou um código simples para verificar se tudo estava funcionando perfeitamente.

Ao inserir o Raspberry Pi Pico em uma placa de prototipagem e conectar o cabo micro USB, você deu os primeiros passos essenciais para começar a programar este microcontrolador.

Além disso, você compreendeu a importância de adicionar o firmware MicroPython ao Raspberry Pi Pico e como fazê-lo utilizando o Thonny. A instalação bem-sucedida do firmware abre um mundo de possibilidades para o desenvolvimento de projetos incríveis com o seu Raspberry Pi Pico.

Estamos apenas começando esta jornada emocionante! No próximo capítulo, vamos explorar ainda mais o potencial do Thonny e do Raspberry Pi Pico, mergulhando mais fundo no desenvolvimento de programas e projetos emocionantes. Continue praticando e explorando este vasto mundo da computação física. Até breve!
