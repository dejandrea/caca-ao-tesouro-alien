import pgzrun
from pygame import Rect
import math
import random

# Inicialização de variáveis
WIDTH = 900
HEIGHT = 700
GAME_STATE = "PLAY" #TODO:APAGAR
# GAME_STATE = "START" 
sounds_on = True
score = 0
lives = 3
stage = 1 #TODO: Mudar para 0
coins = 0

#background
background = Actor("bg1")
background.x = WIDTH // 2
background.y = HEIGHT // 2
background.images = ["bg1","bg2","bg3"]
background.frame = 0
bg_x = 0;

#Jogador


#Inimigos
enemies = []
enemies_images = [["enimie01-1","enimie01-2","enimie01-3"],
                  ["enimie02-1","enimie02-2","enimie02-3"],
                  ["enimie03-1","enimie03-2","enimie03-3"]
                  ]

#blocos invisíveis
invisible_blocks_stg1 = [
    Rect(16, 105, 200, 70),
    Rect(306, 86, 70, 20),
    Rect(0, 360, 300, 70),
    Rect(295, 430, 195, 70),
    Rect(470, 125, 205, 70),
    Rect(460, 485, 50, 70),
    Rect(630, 480, 205, 70),
    Rect(793, 345, 340, 70), #bloco com 5
]

invisible_blocks_stg2 = [
    Rect(0, 345, 155, 20), #bloco com 5
    Rect(0,133, 70, 50), #cogumelo
    Rect(118, 93, 200, 20), #nuvem
    Rect(223, 224, 200, 20), #bloco triplo
    Rect(418, 376, 340, 20), #bloco com 5
    Rect(537, 262, 200, 20), #bloco triplo
    Rect(552, 59, 165, 50), #cogumelo
    Rect(752, 53, 200, 20), #nuvem
    Rect(825, 342, 100, 20),
    Rect(405, 90, 70, 20),
]

invisible_blocks_stg3 = [
    Rect(20, 125, 70, 30), #bloco simples
    Rect(118, 260, 70, 30), #bloco simples
    Rect(226, 330, 70, 30), #bloco simples
    Rect(0, 345, 98, 70), #bloco triplo
    Rect(335, 280, 190, 20),
    Rect(677, 105, 200, 20), #nuvem
    Rect(411, 50, 190, 20),
    Rect(451, 420, 200, 70), #bloco triplo
    Rect(362, 487, 555, 70),
    Rect(565, 365, 335, 70),
    Rect(563, 164, 70, 20),            

]

#placas para mudar de fase
plate_stg1 = Rect(830, 294, 60, 60)
plate_stg2 = Rect(850, 290, 60, 60)
plate_stg3 = Rect(850, 300, 60, 60)

#TODO: APAGAR POSIÇÃO DO MOUSE, VARIÁVEIS, FUNÇÃO E DESENHO
mouse_x, mouse_y = 0, 0

def on_mouse_move(pos):
    global mouse_x, mouse_y
    mouse_x, mouse_y = pos  # Atualiza as coordenadas do mouse

class Enemy:
    def __init__(self,enemy_type):
        self.index_frame = 0
        self.enemy_type = enemy_type
        self.images = enemies_images[self.enemy_type]
        # self.velocities = []
        self.direction = random.choice([-1.5, 1.5,-1,1,0.5,-0.5])
        x = random.randint(100, 800)  # Posição X aleatória
        y = random.randint(0, 200)  # Posição Y aleatória
        self.actor = Actor(self.images[self.index_frame], (x, y))
    
    def animate(self):
        self.index_frame += 0.05
        if self.index_frame >= len(self.images):
            self.index_frame = 0  # Reinicia a animação
        self.actor.image = self.images[int(self.index_frame)]

    def move(self):
        self.actor.x += self.direction
        if self.actor.x > WIDTH -50 or self.actor.x < 50:
            self.direction = self.direction*(-1)

        self.actor.y += 0.3
        if self.actor.y > 600:
            self.actor.y = 50

    def collide(self,collisor):
        enemy_collided = any(self.actor.colliderect(block) for block in collisor)

        if enemy_collided:
            self.direction = self.direction*(-1)

    def draw(self):
        self.actor.draw()

class Alien:
    def __init__(self):
        self.actor = Actor('alien1',(40, 56))
        self.images = ["alien1","alien2"]
        self.frame = 0
        self.velocity_y = 0
        self.collided = False
    
    def animate(self):
        self.frame += 0.05
        if self.frame >= len(self.images):
            self.frame = 0  # Reinicia a animação
        self.actor.image = self.images[int(self.frame)]

    def move(self):
        if self.actor.x <= 40:
            self.actor.x = 40
        if keyboard.left :
            self.actor.x -= 2  # Move para a esquerda
        if keyboard.right:
            self.actor.x += 2  # Move para a direita
        if keyboard.up:
            self.actor.y -= 10  # Move para cima
            self.actor_collided = False


    def velocity(self):
        #velocidade Y do alien
        self.actor.y += self.velocity_y
        if not self.collided:
            self.velocity_y += 0.3

    def collide(self,collisor):
        self.collided = any(self.actor.colliderect(block) for block in collisor)

        if self.collided:
            self.velocity_y = 0

    def draw(self):
        self.actor.draw()

class Reward:
    def __init__(self,reward_type):
        self.index_frame = 0
        self.reward_type = reward_type
        self.images = enemies_images[self.reward_type]
        # self.velocities = []
        self.direction = random.choice([-1.5, 1.5,-1,1,0.5,-0.5])
        x = random.randint(100, 800)  # Posição X aleatória
        y = random.randint(0, 200)  # Posição Y aleatória
        self.actor = Actor(self.images[self.index_frame], (x, y))
    
    def animate(self):
        self.index_frame += 0.05
        if self.index_frame >= len(self.images):
            self.index_frame = 0  # Reinicia a animação
        self.actor.image = self.images[int(self.index_frame)]

    def move(self):
        self.actor.x += self.direction
        if self.actor.x > WIDTH -50 or self.actor.x < 50:
            self.direction = self.direction*(-1)

        self.actor.y += 0.3
        if self.actor.y > 600:
            self.actor.y = 50

    def collide(self,collisor):
        reward_collided = any(self.actor.colliderect(block) for block in collisor)

        if reward_collided:
            self.direction = self.direction*(-1)

    def draw(self):
        self.actor.draw()

alien = Alien()

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
        if stage == 1:
            screen.clear()
            screen.fill((255,255,255))  # Cor de fundo branca
            screen.blit("bg1", (bg_x, 0))
            screen.blit("bg1", (bg_x + WIDTH, 0))
            

            alien.draw()
            alien.move()

            if len(enemies) <= 3:
                generate_enemies()

            for enemy in enemies:
                enemy.draw()
                    
            # for block in invisible_blocks_stg1:
            #     screen.draw.rect(block, "red")
            # screen.draw.rect(plate_stg1, "red")

            for enemy in enemies:
                enemy.collide(invisible_blocks_stg1)

            alien.collide(invisible_blocks_stg1)

            for enemy in enemies:
                if collision(alien.actor, enemy.actor):
                    print("inimigo pegou")
                    lives_over()
            
            if alien.actor.y >= HEIGHT:
                lives_over()
            
            if alien.actor.colliderect(plate_stg1) or alien.actor.x > WIDTH-30:
                next_stage()
        if stage == 2:
            screen.clear()
            screen.fill((255,255,255))  # Cor de fundo branca
            screen.blit("bg2", (bg_x, 0))
            screen.blit("bg2", (bg_x + WIDTH, 0))

            alien.draw()
            alien.move()

            if len(enemies) <= 3:
                generate_enemies()

            for enemy in enemies:
                enemy.draw()
                    
            # for block in invisible_blocks_stg1:
            #     screen.draw.rect(block, "red")
            # screen.draw.rect(plate_stg2, "red")
            for enemy in enemies:
                enemy.collide(invisible_blocks_stg2)

            alien.collide(invisible_blocks_stg2)

            for enemy in enemies:
                if collision(alien.actor, enemy.actor):
                    lives_over()
            
            if alien.actor.y >= HEIGHT:
                lives_over()
            
            if alien.actor.colliderect(plate_stg2) or alien.actor.x > WIDTH-30:
                next_stage()
        if stage == 3:
            screen.clear()
            screen.fill((255,255,255))  # Cor de fundo branca
            screen.blit("bg3", (bg_x, 0))
            screen.blit("bg3", (bg_x + WIDTH, 0))

            alien.draw()
            alien.move()

            if len(enemies) <= 3:
                generate_enemies()

            for enemy in enemies:
                enemy.draw()
                    
            # for block in invisible_blocks_stg1:
            #     screen.draw.rect(block, "red")
            # screen.draw.rect(plate_stg3, "red")
            for enemy in enemies:
                enemy.collide(invisible_blocks_stg3)

            alien.collide(invisible_blocks_stg3)

            for enemy in enemies:
                if collision(alien.actor, enemy.actor):
                    lives_over()
            
            if alien.actor.y >= HEIGHT:
                lives_over()
            
            if alien.actor.colliderect(plate_stg3) or alien.actor.x > WIDTH-30:
                next_stage()

        #TODO: APAGAR TESTES DE POSIÇÃO
        # screen.draw.text(f"BGX: {bg_x}, Y: {background.height}", (10, 10), color="black")
        # screen.draw.text(f"AlienX: {ax}", (10, 30), color="black")
        screen.draw.text(f"Mouse: {mouse_x}, {mouse_y}", (mouse_x, mouse_y), fontsize=24, color="red")
        screen.draw.text(f"Stage: {stage}", (10, 10), color="black")
        screen.draw.text(f"Lives: {lives}", (10, 30), color="black")
        screen.draw.text(f"Score: {score}", (10, 50), color="black")
        screen.draw.text(f"Coins: {coins}", (10, 70), color="black")
        

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

    alien.velocity()
    alien.animate()

    if alien.actor.x >= (WIDTH)-20:
        alien.actor.x = (WIDTH)-20
        end_game()

    for enemy in enemies:
        enemy.animate()
        enemy.move()
        # enemy.change_direction()

# Função de Fim de Jogo
def end_game():
    global GAME_STATE
    
    if alien.actor.x >= WIDTH-20 and score >= 3 and stage == 3: #ganhou o jogo
        GAME_STATE = "WIN"
    if alien.actor.x >= WIDTH-20 and stage == 3 and score < 3: #chegou ao fim, mas não completou a missão
        GAME_STATE = "END"
        print("Não completou")
    if lives <= 0: #perdeu o jogo
        GAME_STATE = "END"
        print("Perdeu tudo")

#Função para verificar se ainda tem vidas
def lives_over():
    global lives
    global GAME_STATE
    lives -=1
    if lives > 0:
        alien.actor.y = 0
        alien.actor.x = 30
    else:
        GAME_STATE = "END"

#Função para mudar de stage
def next_stage():
    global stage
    
    if GAME_STATE == "PLAY" and lives > 0 and stage <= 2:
        stage += 1
        background.frame += 1
        alien.actor.x = 30
        alien.actor.y = 0

        for enemy in enemies:
            enemies.remove(enemy)

# Função para gerar os inimigos
def generate_enemies():
    global enemies
    for i in range(0,3):  # Criando 5 inimigos
        enemies.append(Enemy(i))

def rewards_generate():
    pass 

def collision(actor1, actor2):
    return (abs(actor1.x - actor2.x) < 30 and abs(actor1.y - actor2.y) < 30) 

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
    global stage
    GAME_STATE = "PLAY"
    stage = 1
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
