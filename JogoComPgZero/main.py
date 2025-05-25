import random
import pgzrun

from heroi import Heroi
from inimigo import Inimigo

WIDTH = 800
HEIGHT = 600

limits = {
    'left': 40,
    'right': WIDTH - 40,
    'topo': 40,
    'ground': HEIGHT - 40
}


hero = Heroi((WIDTH // 2, HEIGHT - 100))
inimigos = []



clock.schedule_interval(hero.replace_frame, 0.08)


def criar_inimigo():
    print("chamei a função criar inimigo")
    y = random.randint(60, HEIGHT - 60)
    inimigo = Inimigo((700, y))
    clock.schedule_interval(inimigo.replace_frame, 0.2)
    inimigos.append(inimigo)
    print(f"Inimigo criado em {inimigo.actor.pos}")

clock.schedule_interval(criar_inimigo, 2)

def draw():
    screen.clear()
    screen.fill((0,0,0))
    hero.picture()
    for inimigo in inimigos:
        inimigo.picture()


def update():
    speed = 5
    hero.animating = False

    if keyboard.left:
        direction = 'left'
        hero.move_direction(direction, speed, limits)
    elif keyboard.right:
        direction = 'right'
        hero.move_direction(direction, speed, limits)
    elif keyboard.up:
        hero.move_direction('up', speed, limits)
        criar_inimigo()
    elif keyboard.down:
        hero.move_direction('down', speed,  limits)


    for inimigo in inimigos:
        inimigo.move(-3, 0)
    inimigos[:] = [i for i in inimigos if i.actor.right > 0]


pgzrun.go()
