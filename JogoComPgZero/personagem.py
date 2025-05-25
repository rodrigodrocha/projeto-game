class Personagem:
    def __init__(self, position, sprite, WIDTH = 0, HEIGHT = 0):
        from pgzero.actor import Actor

        self.actor = Actor(sprite[0], position)
        self.frames = sprite
        self.frame_actual = 0
        self.animating = False
        self.limits = {
    'left': 40,
    'right': WIDTH - 100,
    'topo': HEIGHT - 150,
    'ground': HEIGHT - 40
}
    def move(self, dx, dy):
        self.actor.x += dx
        self.actor.y += dy
        self.animating = True
    def replace_frame(self):
        if self.animating:
            self.frame_actual = (self.frame_actual + 1) % len(self.frames)
        else:
            self.frame_actual = 0
        self.actor.image = self.frames[self.frame_actual]
    def picture(self):
        self.actor.draw()
