import numpy as np



### 0 = nothing, but only for instruction
### 1 = load
### 2 = store
### 3 = add
### 4 = jump
# [instruction, instrc address]
ram = np.array([[1,3,2,4,0,0], 
                [4,5,4,0,0,1]])
register = 0
print(ram)


cycles = 99999999999999
head = 0
for i in range(cycles):
    mem = ram[:,head]
    instruct = mem[0]
    addr = mem[1]
    if instruct == 1:
        register = ram[1,addr]
    elif instruct == 2:
        ram[1,addr] = register
    elif instruct == 3:
        register += ram[1,addr]
    elif instruct == 4:
        head = addr

    if i % 1 == 0:
        print(register)

    head += 1