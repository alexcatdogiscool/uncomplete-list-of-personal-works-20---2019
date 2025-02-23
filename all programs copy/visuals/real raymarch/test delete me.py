

class one:
    def __init__(self):
        self.name = 'one'

        
class two:
    def __init__(self):
        self.names = 'two'

        
class three:
    def __init__(self):
        self.namess = 'three'


nums = []
ones = []
twos = []
threes = []

for i in range(1):
    i = one()
    ones.append(i)
for i in range(2):
    i = two()
    twos.append(i)
for i in range(3):
    i = three()
    threes.append(i)

nums.append(ones)
nums.append(twos)
nums.append(threes)
ones = 1
twos = 2
threes = 3

for o in nums[1]:
    print(o.names)