import math



class tile:
    def __init__(self, tileType):
        self.tileType = 0# 0=nothing  1=wire(off)  2=wire(on)  3=wire(on)Trail  4=not gate  5 = transistor
    def update(self, up, down, left, right):
        if self.tileType == 0:
            return 0
        if self.tileType == 1:
            if up.tileType == 2 or down.tileType == 2 or left.tileType == 2 or right.tileType == 2:
                return 2
            else:
                return 1
        if self.tileType == 2:
            if up.tileType == 2 or down.tileType == 2 or left.tileType == 2 or right.tileType == 2:
                if up.tileType == 3 or down.tileType == 3 or left.tileType == 3 or right.tileType == 3:
                    return 3
                else:
                    return 2
            else:
                return 3
        if self.tileType == 3:
            return 1
        
        if self.tileType == 4:
            if left.tileType == 2:
                right.tileType = 3
            else:
                right.tileType = 2
            return 4
        
        if self.tileType == 5:
            if left.tileType == 2:
                up.tileType, down.tileType = down.tileType, up.tileType
            else:
                down.tileType = 3
            return 5
            