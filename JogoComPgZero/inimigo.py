from personagem import Personagem

class Inimigo(Personagem):
    def __init__(self, posicao):
        super().__init__(posicao, ['inimigo_left01'])

    def update(self):
        # Movimento do inimigo vindo da direita para a esquerda
        self.move(-3, 0)

    def fora_da_tela(self):
        return self.actor.right < 0