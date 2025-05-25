import random
import pgzrun
from heroi import Heroi
from inimigo import Inimigo

WIDTH = 540
HEIGHT = 550
scene_shift = 0

hero = Heroi((50, HEIGHT - 100))
inimigos = []


def draw():
    screen.clear()
    screen.blit('back', (scene_shift % -WIDTH, 0))
    screen.blit('back', ((scene_shift % -WIDTH) + WIDTH, 0))
    hero.picture()
    for inimigo in inimigos:
        inimigo.desenhar(scene_shift)

def update():
    global scene_shift
    speed = 1
    hero.animating = False

    if keyboard.space:
        if not hero.marretando:
            hero.iniciar_marretada()
    else:
        if hero.marretando:
            for inimigo in inimigos:
                if not inimigo.derrotado:
                    dx =abs(inimigo.actor.x - hero.actor.x)
                    dy = abs(inimigo.actor.y - hero.actor.y)
                    if dx < 25 and dy < 25:
                        inimigo.derrotado = True
                        inimigo.pos_mundo = inimigo.actor.x - scene_shift
            hero.encerrar_marretada()

    if not hero.marretando:
        if keyboard.left:
            scene_shift += speed
            direction = 'left'
            hero.move_direction(direction, speed)
            for inimigo in inimigos:
                inimigo.aplicar_scroll(speed)
        elif keyboard.right:
            if random.random() < 0.02:  # 2% de chance a cada movimento
                criar_inimigo()
            scene_shift -= speed
            direction = 'right'
            hero.move_direction(direction, speed)
            for inimigo in inimigos:
                inimigo.aplicar_scroll(-speed)
        elif keyboard.up:
            hero.move_direction('up', speed)
        elif keyboard.down:
            hero.move_direction('down', speed)

    for inimigo in inimigos:
        inimigo.update()

def criar_inimigo():
    y = random.randint(450, 515)
    inimigo = Inimigo((900, y))  # Começa fora da tela à direita
    inimigos.append(inimigo)
pgzrun.go()
