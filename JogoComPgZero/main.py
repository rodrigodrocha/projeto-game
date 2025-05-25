import random
import pgzrun

from pgzero.actor import Actor
from heroi import Heroi

WIDTH = 800
HEIGHT = 600

limits = {
    'left': 40,
    'right': WIDTH - 40,
    'topo': 40,
    'ground': HEIGHT - 40
}


hero = Heroi((WIDTH // 2, HEIGHT - 100))
clock.schedule_interval(hero.replace_frame, 0.08)


def draw():
    screen.clear()
    screen.fill((0,0,0))
    hero.picture()


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
        hero.animated = False
    elif keyboard.down:
        hero.move_direction('down', speed,  limits)
        hero.animated = False
    else:
        hero.animated = False


pgzrun.go()
