import pgzrun
from pygame import Rect
import math
import random

# Inicialização de variáveis
WIDTH = 700
HEIGHT = 700
GAME_STATE = "PLAY"

#background
background = Actor("background")
background.x = WIDTH // 2
background.y = HEIGHT // 2
bg_x = 0;

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
        screen.fill((255,255,255))  # Cor de fundo branca
        screen.blit("background", (bg_x, 0))
        screen.blit("background", (bg_x + WIDTH, 0))
        # screen.draw.text(f"BGX: {bg_x}, Y: {background.height}", (10, 10), color="black")
        screen.draw.text(f"Mouse: {mouse_x}, {mouse_y}", (10, 10), fontsize=24, color="red")
        

    elif GAME_STATE == "WIN":
        screen.draw.text("CONGRATULATIONS!!!", center=(WIDTH // 2, HEIGHT//2), fontsize=100, color="red", align="center")
        

    elif GAME_STATE == "END":
        screen.clear()
        screen.fill((0, 0, 0))  # Cor de fundo preta
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT//2), fontsize=100, color="red", align="center")


def update():
    global bg_x
    # Quando a imagem sair completamente da tela, reposiciona
    if bg_x <= -WIDTH*4:
        bg_x = -WIDTH*4
    if bg_x >= 0:
        bg_x = 0


    


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
