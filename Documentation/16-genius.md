## Capítulo 16: Projeto Genius, o jogo de memória dos anos 80

Seja bem-vindo ao desafio de recriar um clássico dos anos 80! Já ouviu falar do jogo Genius lançado pela Estrela? Imagine a emoção de desenvolver e jogar uma versão própria deste clássico no seu Raspberry Pi Pico usando MicroPython! É isso mesmo! Estamos prestes a mergulhar em uma aventura de aprendizado e diversão enquanto exploramos como esse icônico jogo funciona e o recriamos usando a nossa criatividade e habilidades.

Você terá a oportunidade de colocar em prática todas as habilidades que desenvolveu até aqui. Juntos, vamos enfrentar cada desafio, cada detalhe técnico, e ao final deste projeto, você sairá não apenas com um jogo funcional, mas com uma bagagem de conhecimento e experiência que o levará ainda mais longe. Está pronto para aceitar o desafio?

### Sobre o Jogo Genius

O Genius é um jogo eletrônico de memória e habilidade onde luzes coloridas acendem em sequência. Nossa versão do Genius será criada utilizando 4 LEDs coloridos, 4 botões e um buzzer. 

Os LEDs acenderão em uma sequência aleatória que deverá ser repetida pressionando os botões correspondentes. Cada rodada aumentará a dificuldade, acrescentando mais elementos à sequência. Se a sequência for repetida corretamente, o jogo prosseguirá com mais um elemento adicionado. Por outro lado, um erro na sequência resultará no reinício do jogo.

Se quiser dar uma espiada no jogo original em ação, sugiro pesquisar online para ver como ele funciona. Pode ser bem útil para a você se inspirar para esse projeto.

### Montando o circuito

Monte o circuito conforme as intruções que seguem. Certifique-se de verificar a imagem para referência.

Quatro LEDs de diferentes cores são utilizados para representar os desafios do jogo. Cada cor possui um pino associado no Raspberry Pi Pico. O LED verde está conectado ao pino GP15, o vermelho ao pino GP14, o amarelo ao pino GP13 e o azul ao pino GP12. É importante ressaltar que cada LED precisa ser conectado em série com um resistor (normalmente entre 220Ω e 470Ω) para limitar a corrente e proteger tanto o LED quanto o Raspberry Pi Pico. Conecte o terminal positivo do LED (o mais longo) a um resistor e dele ao pino do Pico. Conecte o terminal negativo do LED (o mais curto) ao terra (GND).

Quatro botões são utilizados para que o jogador possa interagir com o jogo. Cada botão está relacionado a um LED correspondente. O botão verde é conectado ao pino GP16, o vermelho ao pino GP17, o amarelo ao pino GP18 e o azul ao pino GP19. Da mesma forma que os LEDs, os botões devem ter um terminal conectado ao terra (GND) do seu Raspberry Pi Pico.

Um buzzer é usado para gerar os sons do jogo. Ele tem seu terminal positivo (o mais longo) conectado ao pino GP20 do Raspberry Pi Pico e o outro terminal conectado ao terra (GND).

![Circuito do projeto genius](/images/genius-circuit.png "Circuito do projeto genius")

O circuito é montado de maneira a conectar cada componente (LEDs, botões e buzzer) aos pinos correspondentes do Raspberry Pi Pico, permitindo a interação entre eles para criar a experiência do jogo Genius. 

O circuito pode ser montado de diversas maneiras, utilizando os mesmos pinos disponíveis no seu Raspberry Pi Pico. O diagrama apresentado é apenas uma das muitas maneiras de realizar a montagem. Você tem total liberdade para organizar e conectar os componentes da forma que melhor se adeque ao seu projeto!

### Codificando o jogo

É hora de você colocar a mão na massa e criar esse jogo! Abaixo está o código completo. Em seguida, uma explicação detalhada de cada parte para que você entenda como tudo funciona.

Adicione este código a um novo arquivo no Thonny, salve-o em seu Raspberry Pi Pico como `genius.py` e depois execute-o. 

Para ver este circuito em funcionamento no simulador Wokwi, clique [aqui](https://wokwi.com/projects/382830081151586305).

```python
from machine import Pin, PWM, Timer
from time import sleep_ms
from random import choice as random_choice

# Configuração do buzzer
buzzer = PWM(Pin(20))
buzzer.duty_u16(0)  # Inicialmente, o buzzer está desligado

# Mapeamento dos LEDs com pinos correspondentes
leds = {
    "Green": {"pin": Pin(15, Pin.OUT), "tone": 415},
    "Red": {"pin": Pin(14, Pin.OUT), "tone": 310},
    "Yellow": {"pin": Pin(13, Pin.OUT), "tone": 252},
    "Blue": {"pin": Pin(12, Pin.OUT), "tone": 209}
}

# Configuração dos botões
buttons = {
    "Green": {"pin": Pin(16, Pin.IN, Pin.PULL_DOWN), "state": 0, "last_state": 0, "switched": False},
    "Red": {"pin": Pin(17, Pin.IN, Pin.PULL_DOWN), "state": 0, "last_state": 0, "switched": False},
    "Yellow": {"pin": Pin(18, Pin.IN, Pin.PULL_DOWN), "state": 0, "last_state": 0, "switched": False},
    "Blue": {"pin": Pin(19, Pin.IN, Pin.PULL_DOWN), "state": 0, "last_state": 0, "switched": False}
}

def check_buttons(timer):
    """Verifica se algum botão foi pressionado ou solto."""
    for button in buttons.values():
        button["state"] = button["pin"].value()
        if button["state"] != button["last_state"]:
            button["switched"] = True
            button["last_state"] = button["state"]

# Timer para verificar se algum botão foi pressionado
Timer(-1).init(period=25, mode=Timer.PERIODIC, callback=check_buttons)

def create_sequence(skill):
    """Gera uma sequência aleatória de cores para o jogador."""
    sequence = []
    for _ in range(skill):
        random_color = random_choice(list(leds.keys()))
        sequence.append(random_color)
    return sequence

def show_sequence(sequence, step):
    """Reproduz uma parte da sequência para o jogador."""
    speed_settings = [
        (1, 5, 420),    # Sequência de 1 a 5
        (6, 13, 320),   # Sequência de 6 a 13
        (14, 31, 220)   # Sequência de 14 a 31
    ]
    for setting in speed_settings:
        if setting[0] <= step <= setting[1]:
            duration = setting[2]
            break

    for color in sequence[:step]:
        sleep_ms(50)                   
        led = leds[color]
        led["pin"].on()                
        play_tone(int(led["tone"]), duration)
        led["pin"].off()               
        
def start_tone(freq):
    """Inicia a reprodução do som."""
    buzzer.freq(int(freq))
    buzzer.duty_u16(1000)
    
def stop_tone():
    """Pára a reprodução do som."""
    buzzer.duty_u16(0)

def play_tone(freq, duration):
    """Reproduz um tom com uma frequência específica por uma duração determinada."""
    start_tone(freq)
    sleep_ms(duration)
    stop_tone()

def play_victory_tone(led):
    """Reproduz um som de vitória para um LED específico."""
    for _ in range(5):
        led["pin"].on()
        play_tone(led["tone"], 70)
        led["pin"].off()
        sleep_ms(70)

def play_losing_tone():
    """Reproduz um som de derrota para todos os LEDs."""
    start_tone(42)
    for _ in range(5):
        for led in leds.values():
            led["pin"].on()
            sleep_ms(30)
            led["pin"].off()
            sleep_ms(30)
    stop_tone()

def is_move_correct(sequence, moves):
    """Verifica se a jogada do jogador está correta."""
    for i in range(len(moves)):
        if moves[i] != sequence[i]:
            return False
    return True

def get_pressed_button():
    """Verifica se algum botão foi pressionado."""
    for color, button in buttons.items():
        if button["switched"]:
            button["switched"] = False
            if button["state"] == 1:
                return color
    return None    

def is_button_released(color):
    """Verifica se um botão foi solto."""
    button = buttons[color]
    if button["switched"]:
        button["switched"] = False
        if button["state"] == 0:
            return color
    return None

def main():
    """Função principal do jogo."""
    skill_level = 3
    new_game = True
    
    while True:
        if new_game:  # Reseta o jogo
            new_game = False
            sleep_ms(500)
            player_moves = []
            current_step = 1
            game_sequence = create_sequence(skill_level)
            show_sequence(game_sequence, current_step)
            
        # Aguarda até um botão ser pressionado
        color_pressed = None
        while color_pressed is None:
            sleep_ms(5)
            color_pressed = get_pressed_button()
        
        # Adiciona cor na lista de movimentos do jogador
        player_moves.append(color_pressed)
        
        # Inicia a reprodução do som e acende o led associado à cor
        led = leds[color_pressed]
        led["pin"].on()
        start_tone(int(led["tone"]))
        
        # Aguarda até que o botão seja liberado
        while not is_button_released(color_pressed):
            sleep_ms(5)
        
        # Pára a reprodução de som e desliga o led
        stop_tone()
        led["pin"].off()
        
        # Avalia a jogada do jogador:
        # - Se correta na última rodada: vitória, novo jogo mais difícil.
        # - Se correta, avança para a próxima cor na sequência.
        # - Se incorreta, toca som de derrota e inicia novo jogo fácil.
        if is_move_correct(game_sequence, player_moves):
            if len(player_moves) == skill_level:
                play_victory_tone(led)
                skill_level += 1
                new_game = True
            elif len(player_moves) == current_step:
                sleep_ms(500)
                player_moves = []
                current_step += 1
                show_sequence(game_sequence, current_step)
        else:
            play_losing_tone()
            skill_level = 3
            new_game = True

# Inicia e controla o fluxo principal do jogo
main()
```

Programa 15.

Chegou a hora de explorarmos cada linha do código juntos! Vamos investigar passo a passo para entender em detalhes como esse código funciona.

```python
from machine import Pin, PWM, Timer
from time import sleep_ms
from random import choice as random_choice
```

Esse trecho de código é responsável por importar funcionalidades especiais que nosso programa usará para interagir com o hardware do Raspberry Pi Pico.

- `from machine import Pin, PWM, Timer`: Aqui, estamos importando algumas funcionalidades básicas para controlar os componentes físicos do nosso dispositivo. O `Pin` nos permite interagir com os pinos do Pico, o `PWM` é usado para controlar a saída de áudio do nosso buzzer, e o `Timer` nos ajuda a criar um temporizador para realizar ações em intervalos específicos.

- `from time import sleep_ms`: Essa linha traz uma função chamada `sleep_ms`, que é usada para criar pausas ou atrasos em milissegundos no nosso programa. Isso é útil para criar intervalos de tempo entre as ações que queremos executar.

- `from random import choice as random_choice`: Aqui estamos importando a função `choice` da biblioteca `random` e renomeando ela para `random_choice`. Essa função será usada para fazer escolhas aleatórias durante o jogo, como a seleção de cores para a sequência no nosso Genius.

```python
# Configuração do buzzer
buzzer = PWM(Pin(20))
buzzer.duty_u16(0)  # Inicialmente, o buzzer está desligado
```

Esse trecho de código é responsável por configurar o buzzer, que é um componente usado para produzir sons no nosso jogo. 

- `buzzer = PWM(Pin(20))`: Aqui, estamos criando uma variável chamada buzzer e a associando ao componente do tipo PWM conectado ao pino físico **GP20** do Raspberry Pi Pico que também tem a função PWM. O PWM é uma técnica usada para controlar a quantidade de energia que é entregue ao buzzer, o que nos permite controlar a frequência e o volume do som emitido.

- `buzzer.duty_u16(0)`: Ao atribuir 0 ao duty_u16, estamos dizendo que inicialmente o buzzer está desligado. 

```python
# Mapeamento dos LEDs com pinos correspondentes
leds = {
    "Green": {"pin": Pin(15, Pin.OUT), "tone": 415},
    "Red": {"pin": Pin(14, Pin.OUT), "tone": 310},
    "Yellow": {"pin": Pin(13, Pin.OUT), "tone": 252},
    "Blue": {"pin": Pin(12, Pin.OUT), "tone": 209}
}
```

Esse trecho de código cria um mapeamento entre as cores dos LEDs e os pinos correspondentes no Raspberry Pi Pico. 

- `leds = { ... }`: Aqui estamos criando um dicionário chamado leds, que associa cada cor verde, vermelho, amarelo e azul com as informações necessárias para controlar cada LED.

- `"Green": {"pin": Pin(15, Pin.OUT), "tone": 415}`: Este é um exemplo de um item no dicionário leds. Para o LED verde, estamos associando a cor "Green" ao dicionário interno `{"pin": Pin(15, Pin.OUT), "tone": 415}`. Isso significa que o LED verde está conectado ao pino `GP15` do Raspberry Pi Pico e configurado como saída `Pin.OUT`. Além disso, estamos atribuindo um tom (frequência do som) de 415 Hz a este LED.

- Similarmente, para os LEDs vermelho, amarelo e azul, estamos definindo os pinos aos quais estão conectados e as frequências de tom correspondentes: LED vermelho (pino `GP14`, frequência 310), LED amarelo (pino `GP13`, frequência 252) e LED azul (pino `GP12`, frequência 209).

Esse dicionário nos permitirá controlar cada LED separadamente, acendendo-os e configurando a frequência do som associado a cada cor específica durante o jogo.

```python
# Configuração dos botões
buttons = {
    "Green": {"pin": Pin(16, Pin.IN, Pin.PULL_DOWN), "state": 0, "last_state": 0, "switched": False},
    "Red": {"pin": Pin(17, Pin.IN, Pin.PULL_DOWN), "state": 0, "last_state": 0, "switched": False},
    "Yellow": {"pin": Pin(18, Pin.IN, Pin.PULL_DOWN), "state": 0, "last_state": 0, "switched": False},
    "Blue": {"pin": Pin(19, Pin.IN, Pin.PULL_DOWN), "state": 0, "last_state": 0, "switched": False}
}

def check_buttons(timer):
    """Verifica se algum botão foi pressionado ou solto."""
    for button in buttons.values():
        button["state"] = button["pin"].value()
        if button["state"] != button["last_state"]:
            button["switched"] = True
            button["last_state"] = button["state"]

# Timer para verificar se algum botão foi pressionado
Timer(-1).init(period=25, mode=Timer.PERIODIC, callback=check_buttons)
```

Esse trecho de código configura os botões do jogo e verifica se algum deles foi pressionado. 

- `buttons = { ... }`: Aqui estamos definindo um conjunto de botões que representam as cores do jogo verde, vermelho, amarelo e azul. Cada botão é representado por um dicionário contendo várias informações.

- `"pin": Pin(numero_pino, Pin.IN, Pin.PULL_DOWN)`: Esta linha configura o pino físico do Raspberry Pi Pico ao qual o botão está conectado. O `Pin(numero_pino)` atribui o número do pino, `Pin.IN` define o pino como entrada, e `Pin.PULL_DOWN` configura o pull-down resistor no pino para evitar flutuações de sinal.

- `"state": 0, "last_state": 0, "switched": False`: Aqui estamos inicializando três variáveis para cada botão. `state` armazena o estado atual do botão (se está pressionado ou não), `last_state` guarda o estado anterior e `switched` indica se houve mudança no estado do botão.

- `def check_buttons(timer): ...`: Esta é uma função que verifica se algum botão foi pressionado ou solto. Ela é chamada periodicamente por um timer para checar os botões em intervalos regulares.

- `Timer(-1).init(period=25, mode=Timer.PERIODIC, callback=check_buttons)`: Aqui estamos inicializando um timer para verificar se algum botão foi pressionado. O timer é configurado para chamar a função `check_buttons` a cada 25 milissegundos `period=25`. Ele funciona de maneira periódica para verificar os estados dos botões, garantindo que qualquer pressionamento seja detectado rapidamente.
Esses botões serão a forma como o jogador interage com o jogo, pressionando-os conforme as sequências de cores forem exibidas pelo jogo, e a função `check_buttons` estará constantemente verificando se esses botões foram pressionados ou soltos.

```python
def create_sequence(skill):
    """Gera uma sequência aleatória de cores para o jogador."""
    sequence = []
    for _ in range(skill):
        random_color = random_choice(list(leds.keys()))
        sequence.append(random_color)
    return sequence

def show_sequence(sequence, step):
    """Reproduz uma parte da sequência para o jogador."""
    speed_settings = [
        (1, 5, 420),    # Sequência de 1 a 5
        (6, 13, 320),   # Sequência de 6 a 13
        (14, 31, 220)   # Sequência de 14 a 31
    ]
    for setting in speed_settings:
        if setting[0] <= step <= setting[1]:
            duration = setting[2]
            break

    for color in sequence[:step]:
        sleep_ms(50)                   
        led = leds[color]
        led["pin"].on()                
        play_tone(int(led["tone"]), duration)
        led["pin"].off() 
```

Esse trecho de código tem duas funções importantes para o jogo:

-  `def create_sequence(skill): ...`: Esta função gera uma sequência aleatória de cores que será apresentada ao jogador durante o jogo. Ela recebe como entrada `skill`, que representa o nível de habilidade ou a quantidade de cores na sequência. Aqui está o passo a passo do que acontece:
    - `sequence = []`: Cria uma lista vazia chamada `sequence` para armazenar a sequência de cores.
    - `for _ in range(skill):`: Itera `skill` vezes para criar a sequência de cores aleatórias.
    - `random_color = random_choice(list(leds.keys()))`: Seleciona uma cor aleatória do conjunto de cores disponíveis (`list(leds.keys())`) usando a função `random_choice`.
    - `sequence.append(random_color)`: Adiciona a cor aleatória à sequência.
    - Por fim, retorna a sequência gerada.

-  `def show_sequence(sequence, step): ...`: Esta função reproduz uma parte da sequência de cores gerada pela função anterior para mostrar ao jogador. Ela recebe como entrada `sequence`, que é a sequência de cores gerada, e `step`, que representa a etapa atual da sequência a ser exibida.
    - `speed_settings = [...]`: Define as configurações de velocidade para exibir a sequência com diferentes durações, dependendo do passo atual (`step`).
    - O loop `for color in sequence[:step]:` percorre as cores na sequência até a etapa atual. Para cada cor, obtém o LED associado à cor atual na sequência, liga o LED correspondente à cor, produz um tom com a frequência associada à cor por uma determinada duração e finalmente desliga o LED após reproduzir a cor por um tempo.

Essas funções são essenciais para mostrar a sequência de cores ao jogador e reproduzir as cores e tons correspondentes a cada rodada do jogo.

```python
def start_tone(freq):
    """Inicia a reprodução do som."""
    buzzer.freq(int(freq))
    buzzer.duty_u16(1000)
    
def stop_tone():
    """Pára a reprodução do som."""
    buzzer.duty_u16(0)

def play_tone(freq, duration):
    """Reproduz um tom com uma frequência específica por uma duração determinada."""
    start_tone(freq)
    sleep_ms(duration)
    stop_tone()
```

Essas funções são usadas para controlar o buzzer, permitindo que ele emita sons com diferentes frequências e durações, criando assim os tons usados no jogo para representar as cores.

- `def start_tone(freq): ...`: Esta função é responsável por iniciar a reprodução do som. Ela recebe como entrada `freq`, que representa a frequência do som a ser reproduzido.
    - `buzzer.freq(int(freq))`: Define a frequência do som no buzzer para a frequência especificada.
    - `buzzer.duty_u16(1000)`: Configura o buzzer para emitir som, ajustando a intensidade do som para um valor específico (1000 neste caso).

- `def stop_tone(): ...`: Esta função pára a reprodução do som. Ela interrompe o som que estava sendo reproduzido.
    - `buzzer.duty_u16(0)`: Configura o buzzer para que não emita nenhum som, colocando-o em silêncio.

- `def play_tone(freq, duration): ...`: Esta função reproduz um tom com uma frequência específica por uma determinada duração.
    - `start_tone(freq)`: Inicia a reprodução do som com a frequência fornecida.
    - `sleep_ms(duration)`: Aguarda por um período de tempo determinado `duration` antes de interromper o som.
    - `stop_tone()`: Desliga a reprodução do som após a duração especificada.

```python
def play_victory_tone(led):
    """Reproduz um som de vitória para um LED específico."""
    for _ in range(5):
        led["pin"].on()
        play_tone(led["tone"], 70)
        led["pin"].off()
        sleep_ms(70)

def play_losing_tone():
    """Reproduz um som de derrota para todos os LEDs."""
    start_tone(42)
    for _ in range(5):
        for led in leds.values():
            led["pin"].on()
            sleep_ms(30)
            led["pin"].off()
            sleep_ms(30)
    stop_tone()
```

Essas funções são utilizadas para criar efeitos sonoros que correspondem às situações de vitória e derrota no jogo, proporcionando uma experiência mais imersiva para os jogadores.

- `def play_victory_tone(led): ...`: Esta função reproduz um som de vitória para um LED específico. Ela faz o último LED pressionado pelo jogador piscar enquanto reproduz um som breve. `for _ in range(5): ...` faz o código indentado ser executado cinco vezes para criar uma breve sequência de piscadas e reprodução de som.
    - `led["pin"].on()`: Acende o LED associado.
    - `play_tone(led["tone"], 70)`: Emite um tom com a frequência do LED (especificada por `led["tone"]`) por um curto período de tempo de 70 milissegundos.
    - `led["pin"].off()`: Desliga o LED.
    - `sleep_ms(70)`: Aguarda um curto intervalo antes de repetir o processo.

- `def play_losing_tone(): ...`: Esta função reproduz um som de derrota usando todos os LEDs. Ela emite um som específico para representar uma situação de derrota no jogo.
    - `start_tone(42)`: Inicia a reprodução de um som específico para indicar a derrota.
    - `for _ in range(5): ...`: Este loop é executado cinco vezes para criar uma sequência de piscadas. Isso é feito iterando por todos os LEDs do jogo, acendendo e apagando cada um deles, em sequência, por 5 vezes.
    - `stop_tone()`: Finaliza a reprodução do som de derrota.

```python
def is_move_correct(sequence, moves):
    """Verifica se a jogada do jogador está correta."""
    for i in range(len(moves)):
        if moves[i] != sequence[i]:
            return False
    return True

def get_pressed_button():
    """Verifica se algum botão foi pressionado."""
    for color, button in buttons.items():
        if button["switched"]:
            button["switched"] = False
            if button["state"] == 1:
                return color
    return None    

def is_button_released(color):
    """Verifica se um botão foi solto."""
    button = buttons[color]
    if button["switched"]:
        button["switched"] = False
        if button["state"] == 0:
            return color
    return None
```

Essas funções são cruciais para verificar se o jogador pressionou os botões corretamente e se esses movimentos correspondem à sequência esperada no jogo.

- `def is_move_correct(sequence, moves):`: Esta função compara a sequência de jogadas do jogador com a sequência gerada pelo jogo. Ela verifica se cada movimento feito pelo jogador está na ordem correta em relação à sequência esperada pelo jogo. Se os movimentos do jogador estiverem na ordem certa em relação à sequência do jogo, a função retorna `True`. Caso contrário, retorna `False`, indicando que pelo menos um dos movimentos do jogador está incorreto. Note que a variável `sequence` é a lista que contém a sequência de cores do jogo atual, e `moves` é uma lista que contém os movimentos do jogador até esse momento.

- `def get_pressed_button():`: Aqui, estamos verificando se algum botão foi pressionado. A função percorre todos os botões disponíveis no jogo e verifica se algum deles foi pressionado. Se algum botão foi pressionado, essa função retorna a cor do botão pressionado. Se nenhum botão foi pressionado, ela retorna `None`.

- `def is_button_released(color):`: Essa função verifica se um botão específico foi solto após ser pressionado. Recebe como parâmetro a cor do botão a ser verificado. Se o botão estiver solto, a função retorna `True`. Caso contrário, retorna `False`, indicando que o botão ainda está pressionado.

```python
def main():
    """Função principal do jogo."""
    skill_level = 3
    new_game = True
```

A função `main()` controla todas as etapas do jogo, desde o início até a avaliação das jogadas do jogador e o reinício do jogo quando necessário.
- `skill_level = 3`: Define o nível de dificuldade inicial do jogo como 3, representando o número de cores na sequência inicial.
- `new_game = True`: Define uma variável para controlar o início de um novo jogo.

```python
    while True:
        if new_game:  # Reseta o jogo
            new_game = False
            sleep_ms(500)
            player_moves = []
            current_step = 1
            game_sequence = create_sequence(skill_level)
            show_sequence(game_sequence, current_step)
```

- `while True:`: Este é um loop infinito que mantém o jogo em execução indefinidamente.
- `if new_game:`: Se `new_game` for `True`, significa que é necessário iniciar um novo jogo.
  - `new_game = False`: Define `new_game` como `False`, indicando que o jogo está em execução.
  - `sleep_ms(500)`: Pausa o jogo por 500 milissegundos (0.5 segundo) antes de começar um novo jogo.
  - `player_moves = []`: Inicializa uma lista vazia para armazenar as jogadas do jogador.
  - `current_step = 1`: Define a etapa atual do jogo como 1.
  - `game_sequence = create_sequence(skill_level)`: Cria uma nova sequência de cores baseada no nível de dificuldade.
  - `show_sequence(game_sequence, current_step)`: Mostra ao jogador a sequência de cores para a primeira etapa do jogo.

```python
        color_pressed = None
        while color_pressed is None:
            sleep_ms(5)
            color_pressed = get_pressed_button()
```

- Este bloco de código aguarda até que um botão seja pressionado pelo jogador. Ele continua verificando a cada 5 milissegundos se um botão foi pressionado. Somente após um botão ser pressionado o código segue.

```python
        player_moves.append(color_pressed)
        led = leds[color_pressed]
        led["pin"].on()
        start_tone(int(led["tone"]))
```

- `player_moves.append(color_pressed)`: Adiciona a cor pressionada à lista de movimentos do jogador.
- `led = leds[color_pressed]`: Atribui o LED associado à cor pressionada à variável `led`.
- `led["pin"].on()`: Acende o LED associado à cor pressionada.
- `start_tone(int(led["tone"]))`: Inicia a reprodução de som correspondente à cor pressionada.

```python
        while not is_button_released(color_pressed):
            sleep_ms(5)
        
        stop_tone()
        led["pin"].off()
```

Este bloco aguarda até que o botão pressionado seja liberado antes de prosseguir. Continua verificando a cada 5 milissegundos.
- `stop_tone()`: Interrompe a reprodução de som.
- `led["pin"].off()`: Desliga o LED associado à cor pressionada.

```python
        if is_move_correct(game_sequence, player_moves):
            if len(player_moves) == skill_level:
                play_victory_tone(led)
                skill_level += 1
                new_game = True
            elif len(player_moves) == current_step:
                sleep_ms(500)
                player_moves = []
                current_step += 1
                show_sequence(game_sequence, current_step)
        else:
            play_losing_tone()
            skill_level = 3
            new_game = True
```

Este bloco avalia se a jogada do jogador está correta.
- Se estiver correta e o jogador completar a sequência:
  - Toca um som de vitória.
  - Aumenta o nível de dificuldade.
  - Define `new_game` como `True` para iniciar um novo jogo.
- Se a jogada estiver incorreta:
  - Toca um som de derrota.
  - Reinicia o nível de dificuldade para 3.
  - Define `new_game` como `True` para iniciar um novo jogo.

### Exercícios

#### Exercício 16.1: Adicionar um Novo Som

Experimente trocar a frequencia de uma das notas musicais utilizadas no jogo. Jogue e verifique a mudança na usabilidade do jogo.

#### Exercício 16.2: Implementar Pontuação

Adicione um sistema de pontuação ao jogo para rastrear o desempenho do jogador. Faça o seguinte:

- Introduza uma variável de pontuação e atualize-a conforme o jogador avança no jogo.
- Aumente a pontuação sempre que o jogador acertar a sequência correta e diminua a pontuação ou reinicie-a se o jogador cometer um erro.
- Exiba a pontuação em um display OLED para que o jogador possa acompanhar seu progresso.

### Conclusão

Maravilha! Chegamos ao fim! Parabéns por essa incrível jornada! Durante esse projeto, você mergulhou fundo no mundo da eletrônica e programação, explorando o jogo Genius com a Raspberry Pi Pico e o MicroPython. Ao longo desse caminho, você enfrentou desafios empolgantes e adquiriu conhecimentos valiosos.

Você aprendeu a criar sequências aleatórias de cores, a controlar LEDs, botões e buzzer. Desenvolveu algoritmos para verificar suas jogadas e gerenciar cada etapa do jogo. Explorou conceitos de lógica, funções, loops e temporizadores.

Continue explorando, desafiando-se e aprendendo. Você é a próxima geração de inovadores! O futuro está nas suas mãos. Continue sonhando, criando e transformando o mundo ao seu redor com as habilidades incríveis que você conquistou. Sucesso!