import random

from personagem import Personagem

class Inimigo(Personagem):
    def __init__(self, position):
        frames = ['heropos03left']
        super().__init__(position, frames)

