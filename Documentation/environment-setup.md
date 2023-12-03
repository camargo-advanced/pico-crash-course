## Preparação do ambiente de desenvolvimento

### Instalando o Thonny Python IDE

Você pode instalar a versão mais recente do Thonny IDE no Windows, macOS ou Linux, ou seja, o Thonny está presente em todas as plataformas. Em um navegador da web, acesse [thonny.org](https://thonny.org/). No canto superior direito da janela do navegador, você verá os links de download para **Windows** e **macOS**, além das instruções para **Linux**. Siga as instruções apresentadas de acordo com o seu sistema operacional para instalar o Thonny.

![Links com instruções de instalação do Thonny](/images/links-thonny.png "Links com instruções de instalação do Thonny")

O Thonny Python IDE vem pré-instalado com o suporte para MicroPython. Portanto, quando você instalar o Thonny, já terá a capacidade de programar em MicroPython sem a necessidade de instalar nenhum pacote adicional. 

Agora abra o Thonny a partir do seu iniciador de aplicativos e você será apresentado à sua tela principal. 

![Tela principal do Thonny](/images/thonny-main-screen.png "Tela principal do Thonny")

Você também pode usar o Thonny para escrever código Python padrão. Digite o seguinte na janela principal e depois clique no botão `Run`. 

```Python
print('Hello World!')
```

Não é necessário entender esse código agora. Utilizamos esse procedimento apenas para testar o seu ambiente e garantir que a instalação do Thonny tenha sido bem sucedida. Caso não obtenha o resultado como na figura que segue, repita os procedimentos anteriores.

![Hello World no Thonny](/images/thonny-hello-world.png "Hello World no Thonny")

O botão `Run` está localizado na barra de ferramentas do Thonny, logo abaixo da barra de menus principal e permite executar um programa. 

![Barra de ferramentas do Thonny](/images/thonny-tool-bar.png "Barra de ferramentas do Thonny")

Nessa barra também se encontra o botão `Stop` que é usado para encerrar a execução de um programa. Caso precise, posicione o seu mouse sobre um botão da barra de ferramentas e aguarde parado por alguns segundos. Uma pequena caixa de texto aparecerá com a descrição daquela função.  

### Adicione o firmware MicroPython

Caso esteja ligando pela primeira vez o seu Raspberry Pi Pico, será necessário adicionar o firmware do MicroPython nele.

Primeiramente confirme que cabo micro USB está conectado na porta micro USB do seu Pico. Agora encontre o botão `BOOTSEL` no seu Raspberry Pi Pico.

![Localização do botão BOOTSEL](/images/pico-bootsel.png "Localização do botão BOOTSEL")

Pressione o botão `BOOTSEL` e mantenha-o pressionado enquanto conecta a outra ponta do cabo micro USB ao seu computador. Uma imagem de um Raspberry Pi é mostrada a seguir, mas o mesmo se aplica a qualquer outro computador.

![Cabo USB sendo conectado ao seu computador](/images/pico-usb-connection.png "Cabo USB sendo conectado ao seu computador")

Após conectar o cabo micro USB ao seu computador, solte o botão `BOOTSEL`. Isso coloca o seu Raspberry Pi Pico no 'modo de dispositivo de armazenamento em massa USB'.

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
