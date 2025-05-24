import random

import pgzrun
from pgzero.actor import Actor

WIDTH = 800
HEIGHT = 600

# Nave
hero = Actor('hero')
hero.pos = WIDTH // 2, HEIGHT - 100

# Frames de animação
hero_frames = ['hero', 'heropos01','heropos02','heropos03']
frame_atual = 0

# Controle da animação
animando = False

def trocar_frame():
    global frame_atual
    if animando:
        frame_atual = (frame_atual + 1) % len(hero_frames)
        hero.image = hero_frames[frame_atual]
    else:
        hero.image = hero_frames[0]  # Fica no frame inicial parado

# Roda a troca de frames a cada 0.2 segundos
clock.schedule_interval(trocar_frame, 0.08)

lixos = []

# Pontuação
pontos = 0

# Gerar lixo
def gerar_lixo():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    lixo = Actor('heropos02left')
    lixo.pos = (x, y)
    lixos.append(lixo)

# Gerar 5 lixos no início
for _ in range(5):
    gerar_lixo()

# Desenhar na tela
def draw():
    screen.clear()
    screen.fill((0, 0, 0))  # Se tiver fundo
    hero.draw()
    for lixo in lixos:
        lixo.draw()
    screen.draw.text(f"Pontos: {pontos}", (10, 10), color="white", fontsize=40)

def update():
    global animando

    velocidade = 5
    movendo = False

    if keyboard.left and hero.x > 50:
        hero.x -= velocidade
        movendo = True
    if keyboard.right and hero.x < WIDTH - 50:
        hero.x += velocidade
        movendo = True
    coletar_lixo()
    animando = movendo  # Ativa animação se estiver movendo

def coletar_lixo():
    global pontos
    for lixo in lixos:
        if hero.colliderect(lixo):
            lixos.remove(lixo)
            pontos += 1
            gerar_lixo()  # Gera outro lixo

pgzrun.go()