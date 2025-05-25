import random
import pgzrun
from heroi import Heroi
from inimigo import Inimigo
from tiro import Tiro

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
tiros = []
pontos = 0
def criar_inimigo():
    print("chamei a função criar inimigo")
    y = random.randint(60, HEIGHT - 60)
    inimigo = Inimigo((WIDTH + 1, y))
    clock.schedule_interval(inimigo.replace_frame, 0.2)
    inimigos.append(inimigo)
    print(f"Inimigo criado em {inimigo.actor.pos}")

def criar_tiro():
    x = hero.actor.x + 40
    y = hero.actor.y
    tiro = Tiro((x, y))
    tiros.append(tiro)
def on_key_down(key):
    if key == keys.SPACE:
        criar_tiro()
def draw():
    screen.clear()
    screen.fill((0,0,0))
    hero.picture()
    for inimigo in inimigos:
        inimigo.picture()
    for tiro in tiros:
        tiro.picture()
    screen.draw.text(
        f"Pontos: {pontos}",
        topleft=(10, 10),
        fontsize=40,
        color="white",
        shadow=(1, 1),
        owidth=0.5,
        ocolor="black"
    )

def update():
    global pontos
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
    elif keyboard.down:
        hero.move_direction('down', speed,  limits)

    for inimigo in inimigos:
        inimigo.move(-3, 0)
    for tiro in tiros:
        tiro.move(10, 0)

    inimigos[:] = [i for i in inimigos if i.actor.right > 0]
    tiros[:] = [t for t in tiros if t.actor.left < WIDTH]

    for tiro in tiros[:]:
        for inimigo in inimigos[:]:
            if tiro.actor.colliderect(inimigo.actor):
                inimigos.remove(inimigo)
                tiros.remove(tiro)
                pontos += 10
                break
clock.schedule_interval(hero.replace_frame, 0.08)
clock.schedule_interval(criar_inimigo, 1)
pgzrun.go()
