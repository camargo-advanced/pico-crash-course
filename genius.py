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