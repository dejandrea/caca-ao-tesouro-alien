import pgzrun
from pygame import Rect
import math
import random

# Inicialização de variáveis
WIDTH = 700
HEIGHT = 700
GAME_STATE = "START"

mouse_x, mouse_y = 0, 0

def on_mouse_move(pos):
    global mouse_x, mouse_y
    mouse_x, mouse_y = pos  # Atualiza as coordenadas do mouse

# Função para desenhar a tela
def draw():
    screen.clear()

    if GAME_STATE == "START":
        screen.fill((0, 0, 0))  # Cor de fundo preta


    elif GAME_STATE == "PLAY":
        screen.clear()
        screen.fill((255,255,255))  # Cor de fundo branca
        

    elif GAME_STATE == "WIN":
        screen.draw.text("CONGRATULATIONS!!!", center=(WIDTH // 2, HEIGHT//2), fontsize=100, color="red", align="center")
        

    elif GAME_STATE == "END":
        screen.clear()
        screen.fill((0, 0, 0))  # Cor de fundo preta
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT//2), fontsize=100, color="red", align="center")


def update():
    pass

    


# Função para iniciar o jogo
def start_game():
    global GAME_STATE
    GAME_STATE = "PLAY"
    print("Jogo Iniciado!")   
    

# Função para sair do jogo
def exit_game():
    print("Saindo do jogo...")
    quit()


# Iniciar o PgZero
pgzrun.go()
