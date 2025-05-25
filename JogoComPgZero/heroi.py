from personagem import Personagem
class Heroi(Personagem):
    def __init__(self, position):
        frames_right = ['hero', 'heropos01', 'heropos02', 'heropos03']

        super().__init__(position, frames_right)

        self.frames_right = frames_right
        self.frames_left = ['heroleft', 'heropos01left', 'heropos02left', 'heropos03left']

    def move_direction(self, way, speed, limits = 0):

        if way == 'left' and self.actor.x > limits['left']:
            self.actor.x -= speed
            self.frames = self.frames_left
            self.animating = True
        elif way == 'right' and self.actor.x < limits['right']:
            self.actor.x += speed
            self.frames = self.frames_right
            self.animating = True
        elif way == 'up' and self.actor.y >= limits['topo']:
            self.actor.y -= speed
        elif way == 'down' and self.actor.y <= limits['ground']:
            self.actor.y += speed
