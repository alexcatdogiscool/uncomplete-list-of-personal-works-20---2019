# or, non, and, nand, xor, xnor, not

def AND(o,t):
    if o == 1 and t == 1:
        return 1
    else:
        return 0

def OR(o,t):
    if o == 1 or t == 1:
        return 1
    else:
        return 0

def NOR(o,t):
    if o == 1 or t == 1:
        return 0
    else:
        return 1

def NAND(o,t):
    if o == 1 and t == 1:
        return 0
    else:
        return 1

def XOR(o,t):
    d = 0
    if o == 1 or t == 1:
        d = 1
    else:
        d = 0
    if o == 1 and t == 1:
        d = 0
    return d

def XNOR(o,t):
    d = 0
    if o == 1 or t == 1:
        d = 0
    else:
        d = 1
    if o == 1 and t == 1:
        d = 1
    return d

def NOT(o,t):
    if o == 1:
        return 0
    else:
        return 1