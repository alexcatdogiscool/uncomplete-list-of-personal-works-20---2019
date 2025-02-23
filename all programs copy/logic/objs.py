import gates

class wire:
    def __init__(self):
        self.sx = 0
        self.sy = 0
        self.ex = 0
        self.ey = 0

        self.slocked = 0
        self.elocked = 0

        self.inlocked = 0
        self.outlocked = 0
        self.iopin = -2

        self.slog = -1
        self.slop = -1

        self.elog = -1
        self.elop = -1

        self.state = 0
    def lock(self, lst, inoutlst):
        self.sx, self.sy = 0,0
        
        if self.slocked == True:
            if self.slop >= lst[self.slog].innum:
                self.sx += lst[self.slog].w
                #self.slop -= lst[self.slog].innum
                self.sy = (30*(self.slop - lst[self.slog].innum))+(lst[self.slog].y)+15
            else:
                self.sy = (30*self.slop)+lst[self.slog].y+15
            self.sx += lst[self.slog].x
        
        if self.elocked == True:
            self.ex, self.ey = 0,0
            if self.elop >= lst[self.elog].innum:
                self.ex += lst[self.elog].w
                #self.elop -= lst[self.elog].innum
                self.ey = (30*(self.elop - lst[self.elog].innum))+(lst[self.elog].y)+15
            else:
                self.ey = (30*self.elop)+lst[self.elog].y+15
            self.ex += lst[self.elog].x

        

        if self.inlocked == 1:
            for ios in inoutlst:
                if ios.pinnum == self.iopin:
                    self.sx = ios.x
                    self.sy = ios.y
        if self.outlocked:
            for ios in inoutlst:
                if ios.pinnum == self.iopin:
                    self.ex = ios.x
                    self.ey = ios.y
    

    def updatestate(self,lst, inoutlst):
        state = lst[self.slog].instate + lst[self.slog].outstate
        self.state = int(state[self.slop])

        if self.inlocked == 1:
            self.state = inoutlst[self.iopin].state
        if self.outlocked == 1:
            inoutlst[self.iopin].state = self.state
            

            

        
        

class gate:
    def __init__(self, name):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.name = name
        self.innum, self.outnum = gates.details(name)
        self.instate = '0' * self.innum
        self.outstate = '0' * self.outnum
    def logic(self):
        self.outstate = gates.layerdlogic(self.instate, str(self.name))
    def updatestate(self, wires, gates):
        t = 0
        for i in gates:
            if i.x == self.x and i.y == self.y:
                gid = t
                break
            t += 1
        for w in wires:
            if w.elog == gid:
                for p in range(self.innum + self.outnum):
                    if w.elop == p:
                        if p < self.innum:
                            s = list(self.instate)
                            s[p] = w.state
                            self.instate = ''.join(map(str, s))
                        if p >= self.innum:
                            tmp1 = w.elog
                            tmp2 = w.elop
                            w.elog = w.slog
                            w.elop = w.slop
                            w.slog = tmp1
                            w.slop = tmp2
                        break

class inout:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = 0
        self.pinnum = 0

        ## 0 = input,  1 = output
        self.mode = 0