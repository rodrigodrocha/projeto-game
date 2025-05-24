import pgzrun
class Personagem:
    def __init__(self, actor, frames_right, frames_left):
        self.actor = actor
        self.frames_right = frames_right
        self.frames_left = frames_left
        self.frames = frames_right
        self.frames_actual = 0
        self.animated = False

        self.speed_y = 0
        self.gravity = 1
        self.ground = True
    def replace_frame(self):
        if self.animated:
            self.frames_actual = (self.frames_actual + 1) % len(self.frames)
            print(self.frames_actual, len(self.frames))
            self.actor.image = self.frames[self.frames_actual]
        else:
            self.actor.image = self.frames[0]

    def draw(self):
        self.actor.draw()


    def move(self, direction, speed, left_limit, right_limit):
        if direction == "left" and self.actor.x > left_limit:
            self.actor.x -= speed
            self.frames = self.frames_left
            self.animated = True
        elif direction == "right" and self.actor.x < right_limit:
            self.actor.x += speed
            #self.frames_actual += 1
            self.frames = self.frames_right
            self.animated = True

    def place_gravity(self, ground_limit):
        self.actor.y += self.speed_y
        self.speed_y += self.gravity

        if self.actor.y >= ground_limit:
            self.actor.y = ground_limit
            self.speed_y = 0
            self.ground = True

    def jump(self):
        if self.ground:
            self.speed_y = - 18
            self.ground = False