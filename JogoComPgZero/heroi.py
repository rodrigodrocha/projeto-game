from personagem import Personagem
from pgzero.clock import clock

class Heroi(Personagem):
    def __init__(self, position, weidth = 540, height = 550):
        frames_right = ['mario-right01','mario-right02']
        super().__init__(position, frames_right, weidth, height)
        self.frames_right = frames_right
        self.frames_left = ['mario-left01', 'mario-left02']
        self.marretando = False
        self.frame_marretada = 0
        self.frames_marretada = ['marretando_right01', 'marretando_right02', 'marretando_right03' ]
    def move_direction(self, way, speed):
        clock.schedule_interval(self.replace_frame, 0.08)
        if way == 'left':
            self.frames = self.frames_left
            self.animating = True
            if self.actor.x > self.limits['left']:
                self.actor.x -= speed
        elif way == 'right':
            self.frames = self.frames_right
            self.animating = True
            if self.actor.x < self.limits['right']:
                self.actor.x += speed
        elif way == 'up' and self.actor.y >= self.limits['topo']:
            self.actor.y -= speed
        elif way == 'down' and self.actor.y <= self.limits['ground']:
            self.actor.y += speed

    def iniciar_marretada(self):
        clock.unschedule(self.replace_frame)
        self.marretando = True
        self.trocar_marretada()
    def trocar_marretada(self):
        if self.frame_marretada < len(self.frames_marretada):
            self.actor.image = self.frames_marretada[self.frame_marretada]
            self.frame_marretada += 1
            clock.schedule_unique(self.trocar_marretada, 0.04)
        else:
            self.actor.image = self.frames_marretada[-1]
            self.frame_marretada = 0
    def finalizar_animacao_marretada(self):
        self.actor.image = self.frames_marretada[1]
        # Fica nesse frame até soltar a tecla

    def encerrar_marretada(self):
        print('encerrar marretada')
        self.marretando = False
        self.actor.image = self.frames[self.frame_actual]