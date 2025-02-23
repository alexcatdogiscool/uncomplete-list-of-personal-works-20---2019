import math

st = 2**0.5

class ray:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

        self.az = 0
        self.el = 0

        self.r = 255
        self.g = 255
        self.b = 255

        self.reflections = 0
        self.hit = False

    def step(self, dst):
        if self.hit == False:
            #hdst = math.cos(self.el) * dst
            #vdst = math.sin(self.el) * dst

            #self.x += math.sin(self.az) * hdst
            #self.y += math.cos(self.az) * hdst
            #self.x += math.sin(self.el) * vdst

            self.x += math.sin(self.az) * dst
            self.y += math.cos(self.az) * dst
            self.z += math.sin(self.el) * dst


    def reflect(self, cx,cy,cz,r):
        ######### HORIZONTAL ########
        xdst = self.x - cx
        ydst = self.y - cy
        atc = math.atan2(ydst, xdst)
        tangent  = atc + (math.pi/2)
        self.az = (tangent - self.az) + tangent


        ######### verticle ########
        zdst = self.z - cz
        ydst = self.y - cy
        atc = math.atan2(ydst, zdst)
        tangent  = atc + (math.pi/2)
        self.el = (tangent - self.el) + tangent