import random

class wall:
    def __init__(self):
        self.x = 800
        self.height = random.randint(200,600)
        self.top = self.height + 90

        ## width is 50px, gap is 90px

    def move(self):
        self.x -= 0.5