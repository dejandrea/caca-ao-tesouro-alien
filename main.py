import pgzrun
from pygame import Rect
import math
import random

# Inicialização de variáveis
WIDTH = 700*4 #TODO: AJUSTAR
HEIGHT = 700
GAME_STATE = "PLAY" #TODO:APAGAR
# GAME_STATE = "START" 
sounds_on = True
score = 0
lives = 3

#background
background = Actor("background")
background.x = WIDTH // 2
background.y = HEIGHT // 2
bg_x = 0;

#Jogador
alien = Actor('alien1')
alien.pos = 100, 56
alien.images = ["alien1","alien2"]
alien.frame = 0
alien.width = 100
alien.height = 100

#blocos invisíveis - #TODO: AGRUPAR BLOCOS SE POSSÍVEL
invisible_block1 = Rect(35, 105, 200, 70)
invisible_block2 = Rect(0, 360, 310, 70)
invisible_block3 = Rect(310, 430, 195, 70)
invisible_block4 = Rect(480, 125, 205, 70)
invisible_block5 = Rect(500, 485, 50, 70)
invisible_block6 = Rect(645, 480, 205, 70)
invisible_block7 = Rect(810, 345, 340, 70) #bloco com 5
invisible_block8 = Rect(900, 140, 165, 50) #cogumelo
invisible_block9 = Rect(1110, 100, 200, 20) #nuvem
invisible_block10 = Rect(1210, 230, 200, 70) #bloco triplo
invisible_block11 = Rect(1405, 380, 340, 70) #bloco com 5
invisible_block12 = Rect(1525, 265, 200, 70) #bloco triplo
invisible_block13 = Rect(1540, 70, 165, 50) #cogumelo
invisible_block14 = Rect(1735, 60, 200, 20) #nuvem
invisible_block15 = Rect(1940, 125, 70, 30) #bloco simples
invisible_block16 = Rect(2060, 220, 70, 30) #bloco simples
invisible_block17 = Rect(1975, 275, 70, 30) #bloco simples
invisible_block18 = Rect(1810, 345, 200, 70) #bloco triplo
invisible_block19 = Rect(2255, 280, 190, 20)
invisible_block20 = Rect(2542, 100, 200, 20) #nuvem
invisible_block21 = Rect(2328, 50, 190, 20)
invisible_block22 = Rect(2365, 420, 200, 70) #bloco triplo
invisible_block23 = Rect(2245, 487, 555, 70)
invisible_block24 = Rect(2478, 365, 320, 70)


#TODO: APAGAR POSIÇÃO DO MOUSE, VARIÁVEIS, FUNÇÃO E DESENHO
mouse_x, mouse_y = 0, 0

def on_mouse_move(pos):
    global mouse_x, mouse_y
    mouse_x, mouse_y = pos  # Atualiza as coordenadas do mouse

# Função para desenhar a tela
def draw():
    screen.clear()

    if GAME_STATE == "START":
        screen.fill((0, 0, 0))
        # Título
        screen.draw.text("Menu Principal", center=(WIDTH // 2, 100), fontsize=50, color="white", align="center")

        # Botão Começar Jogo
        screen.draw.rect(Rect((WIDTH / 2 - 100, 200), (200, 50)), color="blue")
        screen.draw.text("Começar Jogo", center=(WIDTH / 2, 225), fontsize=30, color="white")

        # Botão Ligar/Desligar Sons
        screen.draw.rect(Rect((WIDTH / 2 - 100, 300), (200, 50)), color="green")
        screen.draw.text("Sons: On" if sounds_on else "Sons: Off", center=(WIDTH / 2, 325), fontsize=30, color="white")

        # Botão Sair
        screen.draw.rect(Rect((WIDTH / 2 - 100, 400), (200, 50)), color="red")
        screen.draw.text("Sair", center=(WIDTH / 2, 425), fontsize=30, color="white")


    elif GAME_STATE == "PLAY":
        screen.clear()
        screen.fill((255,255,255))  # Cor de fundo branca
        screen.fill((255,255,255))  # Cor de fundo branca
        screen.blit("background", (bg_x, 0))
        screen.blit("background", (bg_x + WIDTH, 0))

        alien.draw()
        move_player()

        #TODO: APAGAR BLOCOS INVISÍVEIS
        screen.draw.rect(invisible_block1, "red")
        screen.draw.rect(invisible_block2, "red")
        screen.draw.rect(invisible_block3, "red")
        screen.draw.rect(invisible_block4, "red")
        screen.draw.rect(invisible_block5, "red")
        screen.draw.rect(invisible_block6, "red")
        screen.draw.rect(invisible_block7, "red")
        screen.draw.rect(invisible_block8, "red")
        screen.draw.rect(invisible_block9, "red")
        screen.draw.rect(invisible_block10, "red")
        screen.draw.rect(invisible_block11, "red")
        screen.draw.rect(invisible_block12, "red")
        screen.draw.rect(invisible_block13, "red")
        screen.draw.rect(invisible_block14, "red")
        screen.draw.rect(invisible_block15, "red")
        screen.draw.rect(invisible_block16, "red")
        screen.draw.rect(invisible_block17, "red")
        screen.draw.rect(invisible_block18, "red")
        screen.draw.rect(invisible_block19, "red")
        screen.draw.rect(invisible_block20, "red")
        screen.draw.rect(invisible_block21, "red")
        screen.draw.rect(invisible_block22, "red")
        screen.draw.rect(invisible_block23, "red")
        screen.draw.rect(invisible_block24, "red")


        #TODO: APAGAR TESTES DE POSIÇÃO
        # screen.draw.text(f"BGX: {bg_x}, Y: {background.height}", (10, 10), color="black")
        # screen.draw.text(f"AlienX: {ax}", (10, 30), color="black")
        screen.draw.text(f"Mouse: {mouse_x}, {mouse_y}", (mouse_x, mouse_y), fontsize=24, color="red")
        

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

    # movimento do alien
    alien.frame += 0.05  # Ajuste o valor para controlar a velocidade da animação
    if alien.frame >= len(alien.images):
        alien.frame = 0  # Reinicia a animação

    alien.image = alien.images[int(alien.frame)]  # Atualiza a imagem do ator
    if alien.x <= 50:
        alien.x = 50

    if alien.x >= (WIDTH)-20:
        alien.x = (WIDTH)-20
        end_game()

# Função de Fim de Jogo
def end_game():
    global GAME_STATE
    
    if alien.x >= WIDTH-20 and score >= 3: #ganhou o jogo
        GAME_STATE = "WIN"
    elif alien.x >= WIDTH-20 and score < 3: #chegou ao fim, mas não completou a missão
        GAME_STATE = "END"
    elif lives <= 0: #perdeu o jogo
        GAME_STATE = "END"

# Função para movimento do Jogador
def move_player():
    global bg_x
    if keyboard.left :
        # alien.x -= 2  # Move para a esquerda
        bg_x += 2
        invisible_block1.x += 2 #TODO: APAGAR
    if keyboard.right and bg_x > -WIDTH*4:
        # alien.x += 2  # Move para a direita
        bg_x -= 2
        invisible_block1.x -= 2 #TODO: APAGAR
    if keyboard.right and bg_x == -WIDTH*4:
        alien.x += 2  # Move para a direita
        # bg_x -= 2
    if keyboard.up:
        alien.y -= 5  # Move para cima
    if keyboard.down:
        alien.y += 5  # Move para baixo

# Função para verificar cliques do mouse
def on_mouse_down(pos, button):
    global sounds_on

    # Verifica se o botão "Começar Jogo" foi clicado
    if Rect((WIDTH / 2 - 100, 200), (200, 50)).collidepoint(pos):
        start_game()
    
    # Verifica se o botão "Ligar/Desligar Sons" foi clicado
    elif Rect((WIDTH / 2 - 100, 300), (200, 50)).collidepoint(pos):
        sounds_on = not sounds_on  # Alterna o estado dos sons
        toggle_sounds()

    # Verifica se o botão "Sair" foi clicado
    elif Rect((WIDTH / 2 - 100, 400), (200, 50)).collidepoint(pos):
        exit_game()


# Função para iniciar o jogo
def start_game():
    global GAME_STATE
    GAME_STATE = "PLAY"
    print("Jogo Iniciado!")   

# Função para ligar ou desligar os sons
def toggle_sounds():
    #TODO: TROCAR O SOM DE FUNDO E ACRESCENTAR SONS DO JOGO
    if sounds_on:
        sounds.air.play(loops=True)  # Retoma a música de fundo
    else:
        sounds.air.stop()  # Pausa a música de fundo
    
# Função para sair do jogo
def exit_game():
    print("Saindo do jogo...")
    quit()


# Iniciar o PgZero
pgzrun.go()
