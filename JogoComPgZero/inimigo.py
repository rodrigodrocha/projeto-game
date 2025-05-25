from pgzero.clock import clock

from personagem import Personagem

class Inimigo(Personagem):
    def __init__(self, posicao):
        super().__init__(posicao, ['inimigo_left01', 'inimigo_left02', 'inimigo_left03', 'inimigo_left04'])
        self.derrotado = False
        self.pos_mundo = posicao[0]
        self.imagem_derrotado = "inimigo_derrotado1"

        clock.schedule_interval(self.replace_frame, 0.2)
        self.animating = True
    def update(self):
        if not self.derrotado:
            self.move(-1.5, 0)

    def aplicar_scroll(self, dx):
        if not self.derrotado:
            self.move(dx, 0)
        else:
            self.pos_mundo += dx

    def fora_da_tela(self):
        return self.actor.right < 0

    def desenhar(self, scene_shift):
        if self.derrotado:
            self.actor.x = self.pos_mundo + scene_shift
            self.actor.image = self.imagem_derrotado
        self.picture()