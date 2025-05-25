from personagem import Personagem
class Inimigo(Personagem):
    def __init__(self, position):
        frames = ['inimigo', 'inimigo01']
        super().__init__(position, frames)
