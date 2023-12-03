## Projeto: Qual a temperatura?

Este projeto é um mergulho empolgante no universo da tecnologia, permitindo que você crie um circuito que exibirá a temperatura atual em um display OLED, usando o sensor de temperatura interno do chip do Raspberry Pi Pico.

Para isso utilizaremos o protocolo chamado I2C (Inter-Integrated Circuit em inglês), que possibilita a comunicação entre o Raspberry Pi Pico e o display OLED SSD1306. Esse protocolo é uma das maneiras pelas quais dispositivos podem se comunicar entre si. O I2C não só permite a conexão simples e eficiente entre o Pico e o display, mas também é amplamente utilizado para uma variedade de aplicações em projetos de eletrônica e robótica.

Por exemplo, além de exibir a temperatura, o protocolo I2C pode ser empregado para conectar sensores de diferentes tipos, como sensores de umidade, pressão atmosférica, luminosidade e muitos outros ao Raspberry Pi Pico. 

Imagine a variedade de projetos possíveis! Você pode criar um termômetro digital, um monitor de umidade para suas plantas domésticas, um contador de passos em um projeto de wearable, um sistema de controle para um pequeno robô autônomo ou até mesmo um dispositivo de automação residencial. As possibilidades são infinitas!

Preparado para dar vida às suas ideias?

### O Display OLED SSD1306

O display OLED SSD1306 é uma tela pequena, mas poderosa, que nos permite mostrar informações de forma visual e interativa. Ele é um tipo especial de tela que utiliza diodos orgânicos emissores de luz (OLED, Organic Light-Emitting Diode em inglês) para criar imagens nítidas e brilhantes. Mas o que torna o SSD1306 ainda mais interessante é que ele não é apenas um tela, é uma tela inteligente capaz de exibir texto, gráficos e até mesmo pequenas imagens!

![Display OLED SSD1306 visto de frente](/images/oled-ssd1306-front.jpg "Display OLED SSD1306 visto de frente")

Esta tela em particular tem um jeito especial de mostrar cores. Alguns desses displays podem ter as duas primeiras linhas de texto amarelas, enquanto as outras seis linhas são azuis. Isso dá um visual diferente e pode tornar seus projetos mais divertidos e criativos!

### Comunicação entre dispositivos com I2C

Para conectar o display ao Raspberry Pi Pico, usaremos um protocolo de comunicação chamado I2C. Este protocolo é como um caminho para que o Pico converse com o display, permitindo que eles troquem informações. O display OLED SSD1306 possui quatro pinos que usaremos para conectá-lo ao Pico:

- `VCC`: Esse pino fornece energia para o display. Conectamos ele ao pino de 3.3V no Pico.
- `GND`: É o pino de terra, usado para completar o circuito elétrico. Conectamos ele ao GND no Pico.
- `SCL`: Esse pino é para o relógio de sincronização do I2C. Conectamos ele a algum pino com a função SCL no Pico.
- `SDA`: É o pino de dados que permite enviar e receber dados entre o Raspberry Pi Pico e o display. Conectamos ele a algum pino com a função SDA no Pico.

No protocolo I2C, vários dispositivos podem ser conectados ao mesmo barramento compartilhando as linhas SCL e SDA, e cada dispositivo tem um endereço único que o identifica. Um dispositivo coordena a comunicação, iniciando e encerrando as transmissões de dados e direcionando a comunicação para um dispositivo específico através de seu endereço. 

O endereço I2C pode estar impresso na placa do display ou em uma etiqueta na parte de trás do componente. Ele geralmente é um número hexadecimal, como 0x3C ou 0x3D, por exemplo. Este endereço é fundamental para que o Raspberry Pi Pico saiba com qual dispositivo ele está se comunicando quando você escreve o código em MicroPython. No exemplo que segue note que existem duas possibilidades de endereço 0x78 ou 0x7A e que a solda no circuito definiu que o endereço utilizado nesse display é o 0x78. 

![Display OLED SSD1306 visto de trás](/images/oled-ssd1306-back.jpg "Display OLED SSD1306 visto de trás")

Usaremos uma biblioteca chamada `ssd1306` no Raspberry Pi Pico para ajudar a controlar esse display. A biblioteca `ssd1306` é como um conjunto de instruções que dizem ao Pico como usar o display OLED SSD1306. Ela nos permite mostrar texto, números e até mesmo criar pequenas imagens no display, tudo isso de forma bem simples usando a linguagem de programação MicroPython.

### Codificando o projeto

Antes de tudo monte o circuito conectando os pinos `SDA` e `SCL` do Raspberry Pi Pico aos pinos `SDA` e `SCL` do display OLED para comunicação I2C. Além disso, o pino de `3.3V` do Pico deve ser conectado ao pino `VCC` de alimentação do display OLED para fornecer energia, e o pino `GND` do Pico deve ser conectado ao pino de terra `GND` do display OLED para completar o circuito, conforme a imagem que segue.

![Circuito do projeto oled](/images/oled-circuit.png "Circuito do projeto oled")

Agora adicione este código a um novo arquivo no Thonny, salve-o em seu Raspberry Pi Pico como `oled.py` e depois execute-o. 

Para ver este circuito em funcionamento no simulador Wokwi, clique [aqui](https://wokwi.com/projects/382846733223778305).

```python
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from time import sleep_ms

# Configura sensor de temperatura
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

# Configuração do I2C para se comunicar com o módulo OLED
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)  
display = SSD1306_I2C(128, 64, i2c, 0x3C)
sleep_ms(1000)  # Aguarda configuração ser aplicada

while True:
    # Lê sensor de temperatura do Pico e calcula temperatura
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    formatted_temperature = f"{temperature:.1f}"

    # Escreve no display
    display.fill(0)
    display.text("Temperature (C)", 5, 5)
    display.text(formatted_temperature, 50, 27)
    display.show()
    
    sleep_ms(500)  # Aguarda meio segundo
```

Programa 14.

Vamos entender cada uma das linhas desse código juntos.

```python
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
from time import sleep_ms
```

Nesta parte, estamos importando as bibliotecas e módulos necessários para o código funcionar. 

- `machine` é um módulo que oferece acesso a recursos de hardware do Raspberry Pi Pico. `Pin` é usado para controlar os pinos GPIO, `I2C` é usado para comunicação I2C, `ADC` é usado para o conversor analógico-digital e `time` é utilizado para lidar com o tempo. 

- `ssd1306` é a biblioteca para controle do display OLED SSD1306.

```python
# Configura sensor de temperatura
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)
```

O Raspberry Pi Pico possui um sensor de temperatura interno, que é lido no quarto canal do conversor analógico-digital. Assim como o potenciômetro, a saída do sensor é uma voltagem variável: à medida que a temperatura muda, a voltagem também muda.

- Na linha `sensor_temp = ADC(4)` configuramos o conversor analógico-digital, mas em vez de usar o número de um pino, utilizamos o número do canal conectado ao sensor de temperatura interno do Pico. 

- A linha `conversion_factor` converte os valores lidos em tensão para valores de temperatura. Ao dividir a tensão de referência de 3.3 volts pelo valor máximo do ADC de 16 bits (65535), obtemos o fator de conversão. Esse fator será usado para transformar os valores lidos pelo ADC para uma escala de tensão de 0 a 3.3 volts.

```python
# Configuração do I2C para se comunicar com o módulo OLED
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
display = SSD1306_I2C(128, 64, i2c, 0x3C)
sleep_ms(1000)  # Aguarda configuração ser aplicada
```

Nesta parte, estamos configurando a comunicação I2C entre o Raspberry Pi Pico e o display OLED SSD1306. 

- Estamos inicializando um objeto `i2c` para a comunicação I2C usando os pinos 16 (`I2C0 SDA`) e 17 (`I2C0 SCL`) do Pico. 

- O objeto `display` é inicializado como um display SSD1306_I2C com uma resolução de 128x64 pixels e um endereço específico (0x3C) no barramento I2C. 

> **`Importante`**: Lembre de verificar o endereço específico de seu display, olhando na parte de trás dele, e altere o código para refletir esse endereço.

- O `sleep_ms(1000)` é utilizado para aguardar 1 segundo antes do início do loop principal. Esse período garante que a configuração inicial dos dispositivos esteja completa e estabilizada antes de começar a coleta e exibição dos dados.

```python
while True:
    # Lê sensor de temperatura do Pico e calcula temperatura
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    formatted_temperature = f"{temperature:.1f}"
```

Esse trecho de código realiza a leitura do sensor de temperatura, converte essa leitura em uma temperatura em graus Celsius e formata o valor para exibição, garantindo que apenas uma casa decimal seja mostrada no display do OLED.

- `sensor_temp.read_u16()`: Esta linha lê o sensor de temperatura conectado ao Raspberry Pi Pico. O método `read_u16()` lê a tensão analógica e converte para um valor inteiro de 16 bits (0 a 65535).

- `reading = sensor_temp.read_u16() * conversion_factor`: A leitura do sensor, que está na forma de um número inteiro de 16 bits, é multiplicada pelo `conversion_factor`. Este fator de conversão foi calculado anteriormente (`3.3 / 65535`) e é usado para converter o valor lido pelo sensor em uma tensão de 0 a 3.3 volts.
   
- `temperature = 27 - (reading - 0.706) / 0.001721`: Esta linha converte a tensão medida para uma temperatura em graus Celsius. Essa fórmula específica é uma equação de calibração usada para converter a leitura do sensor em temperatura. Essa equação é ajustada para o sensor específico do Raspberry Pi Pico e está contida no seu datasheet.

- `formatted_temperature = f"{temperature:.1f}"`: Aqui é feita a formatação do valor da temperatura para exibir apenas uma casa decimal. O `f"{temperature:.1f}"` usa f-strings do Python para formatar o valor da temperatura (`temperature`) com uma casa decimal (`:.1f`).

```python
# Escreve no display
display.fill(0)
display.text("Temperature (C)", 5, 5)
display.text(formatted_temperature, 50, 27)
display.show()

sleep_ms(500)  # Aguarda meio segundo
```

Esse trecho de código atualiza o display OLED com informações da temperatura. Ele limpa o display, escreve o texto "Temperature (C)" e a temperatura formatada, mostra as alterações no display e, em seguida, aguarda meio segundo antes de continuar para a próxima atualização.

 - `display.fill(0)` limpa o conteúdo atual do display preenchendo-o com zeros (que geralmente representam pixels desligados). Isso garante que o display seja limpo antes de escrever novas informações.

- `display.text("Temperature (C)", 5, 5)` escreve um texto no display OLED. O texto "Temperature (C)" será exibido a uma posição específica no display. Os números 5 e 5 são as coordenadas x e y onde o texto começará a ser exibido.

- `display.text(formatted_temperature, 50, 27)` escreve a temperatura formatada no display OLED. `formatted_temperature` é a temperatura previamente calculada e formatada para exibição com uma casa decimal. Novamente, 50 e 27 representam as coordenadas x e y no display onde o texto será exibido.

- `display.show()` atualiza o display com as informações que foram escritas. Após escrever os textos desejados, essa função exibe o conteúdo no display, mostrando as informações recém-adicionadas.

- `sleep_ms(500)` é uma função que faz o programa aguardar por 500 milissegundos (ou meio segundo) antes de continuar. Essa pausa é útil para controlar a frequência com que as informações são atualizadas no display. No caso, após exibir as informações, o programa espera meio segundo antes de realizar o próximo ciclo de leitura e exibição de temperatura.

Parabéns! Ao finalizar este projeto, você não apenas explorou o incrível potencial do Raspberry Pi Pico e do MicroPython, mas também mergulhou no universo fascinante da eletrônica e programação utilizando um display para apresentar informações. Nos vemos no próximo projeto!
