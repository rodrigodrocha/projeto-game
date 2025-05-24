import random
import pgzrun

from pgzero.actor import Actor
from personagens import Personagem

WIDTH = 800
HEIGHT = 600

# Nave
hero_init = Actor('hero')
hero_init.pos = WIDTH // 2, HEIGHT - 100
# Frames de animação
hero_frames_right = ['hero', 'heropos01','heropos02','heropos03']
hero_frames_left = ['heroleft','heropos01left','heropos02left','heropos03left']

hero = Personagem(hero_init, hero_frames_right, hero_frames_left)
clock.schedule_interval(hero.replace_frame, 0.2)
# Desenhar na tela
def draw():
    screen.fill((0, 0, 0))  # Se tiver fundo
    hero.draw()

def update():

    speed = 5
    ground_limit = HEIGHT - 100

    if keyboard.left:
        hero.move("left", speed, 50, WIDTH - 50)
    elif keyboard.right:
        hero.move("right", speed, 50, WIDTH - 50)
    else:
        hero.animated = False

    if keyboard.space:
        hero.jump()

    hero.place_gravity(ground_limit)


pgzrun.go()