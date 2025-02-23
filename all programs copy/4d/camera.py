import funcs
import math




class camera:
    def __init__(self, fov, screenWidth, screenHeight):
        self.x = 0
        self.y = 0
        self.z = 0
        self.az = 0
        self.el = 0
        self.fov = fov
        self.w = screenWidth
        self.h = screenHeight
    
    def render(self, surface, shapelst):
        for s in shapelst:

            

            s.x -= self.x
            s.y -= self.y
            s.z -= self.z

            """
            dst = funcs.norm(s.x,s.y,s.z)
            sAz = math.atan2(s.x,s.z)

            sAz += self.az
            s.x = math.sin(sAz) * dst
            s.z = math.cos(sAz) * dst
            """

            ########
            s.draw(surface, self.w,self.h, self.fov, self.az)
            ########
            """
            sAz -= self.az
            s.x = math.sin(sAz) * dst
            s.z = math.cos(sAz) * dst
            """
            s.x += self.x
            s.y += self.y
            s.z += self.z