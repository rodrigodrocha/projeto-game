import random
import pgzrun
from heroi import Heroi


WIDTH = 540
HEIGHT = 550
scene_shift = 0
limits = {
    'left': 40,
    'right': WIDTH - 100,
    'topo': HEIGHT - 150,
    'ground': HEIGHT - 40
}
hero = Heroi((50, HEIGHT - 100))

def draw():
    screen.clear()
    screen.blit('back', (scene_shift % -WIDTH, 0))
    screen.blit('back', ((scene_shift % -WIDTH) + WIDTH, 0))
    hero.picture()

def update():
    global scene_shift
    speed = 1
    hero.animating = False

    if keyboard.space:
        if not hero.marretando:
            hero.iniciar_marretada()
    else:
        if hero.marretando:
            hero.encerrar_marretada()

    if not hero.marretando:
        if keyboard.left:
            scene_shift += speed
            direction = 'left'
            hero.move_direction(direction, speed, limits)
        elif keyboard.right:
            scene_shift -= speed
            direction = 'right'
            hero.move_direction(direction, speed, limits)
        elif keyboard.up:
            hero.move_direction('up', speed, limits)
        elif keyboard.down:
            hero.move_direction('down', speed,  limits)


pgzrun.go()
