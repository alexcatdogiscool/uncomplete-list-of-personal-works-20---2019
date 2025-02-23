import math


class ray:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.az = 0
        self.el = 0

        self.r = 0
        self.g = 0
        self.b = 0

        self.shade = 0

        self.running = True
        self.reflected = False

    def step(self, dst, lightaz, lightel):
        if dst < 0.2 and self.reflected == False and self.running == True:
            self.reflected = True
            self.r, self.g, self.b = (255,255,255)
            #self.az = lighaz
            #self.el = lightel

        if self.running == True:
            self.x += math.cos(self.az) * dst
            self.y += math.sin(self.az) * dst
            self.z += math.sin(self.el) * dst

            self.r += self.shade
            self.g += self.shade
            self.b += self.shade