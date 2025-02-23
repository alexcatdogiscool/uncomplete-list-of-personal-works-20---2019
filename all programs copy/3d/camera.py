import funcs
import math




class camera:
    def __init__(self, fov, screenWidth, screenHeight):
        self.x = 0
        self.y = 0
        self.z = 0
        self.w = 0
        self.fov = fov
        self.w = screenWidth
        self.h = screenHeight
    
    def render(self, surface, shapelst):
        for s in shapelst:

            s.x -= self.x
            s.y -= self.y
            s.z -= self.z
            s.w -= self.w   

            s.draw(surface, self.w,self.h, self.fov)
            
            s.x += self.x
            s.y += self.y
            s.z += self.z
            s.w += self.w