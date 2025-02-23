f1 = open('gates.txt','r')
data = f1.read()
f1.close()
funcs = data.split('\n')


def gates(gatename,inp):
    for i in range(len(funcs)):
        name = (funcs[i].split(',')[0])
        if name == gatename:
            gatenum = i
            break
    truth = funcs[gatenum].split(',')[3].split('.')
    truthin = truth[0].split(';')
    truthout = truth[1].split(';')
    innum = funcs[gatenum].split(',')[1]
    for i in range(2**(int(innum))):
        if inp == truthin[i]:
            return truthout[i]
        


def details(gatename):
    if gatename == 'AND':
        return 2, 1
    if gatename == 'NOT':
        return 1, 1
    f = open('newgates.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    del data[-1]
    for i in range(len(data)):
        name = data[i].split('.')[0]
        if name == gatename:
            data = data[i]
    
    ios = data.split('.')[3].split(',')
    ins = 0
    outs = 0
    for i in range(len(ios)):
        if ios[i].split(';')[0] == '0':
            ins += 1
        if ios[i].split(';')[0] == '1':
            outs += 1
    #print(ins, outs)
    return ins, outs












def layerdlogic(inputs, gatename):
    
    if gatename == 'AND':
        if inputs[0] == '1' and inputs[1] == '1':
            return '1'
        else:
            return '0'
    if gatename == 'NOT':
        return str(int(not(int(inputs))))
    


    
    f = open('newgates.txt','r')
    data = f.read()
    f.close()
    
    ##################
    instate = inputs
    ##################
    data = data.split('\n')
    for i in range(len(data)):
        if data[i].split('.')[0] == gatename:
            data = data[i]
    #if type(data) == list:
     #   data = data[0]
              


    
    #newgatename = data.split('.')[0]
    gates = data.split('.')[1].split(',')
    wires = data.split('.')[2].split(',')
    inouts = data.split('.')[3].split(',')
    del gates[-1]
    del wires[-1]
    del inouts[-1]
    #print(newgatename)
    class gate:
        def __init__(self,l, num):
            lst = l.split(';')
            if gatename == 'AND':
                self.name = 'AND'
            if gatename == 'NOT':
                self.name = 'NOT'
            if gatename != 'AND' and gatename != 'NOT':
                self.name = lst[0]
            self.gid = num
            if self.name == 'AND':
                self.innum = 2
                self.outnum = 1
            if self.name == 'NOT':
                self.innum = 1
                self.outnum = 1
            if self.name != 'AND' and self.name != 'NOT':
                self.innum, self.outnum = details(self.name)
            self.instate = '0' * self.innum
            self.outstate = '0' * self.outnum
        def logic(self):
            self.outstate = '0'
            if self.name == 'AND':
                if self.instate[0] == '1' and self.instate[1] == '1':
                    self.outstate = '1'
            if self.name == 'NOT':
                self.outstate = str(int(not(int(self.instate))))
            if self.name != 'AND':
                if self.name != 'NOT':
                    #print(self.name)
                    self.outstate = layerdlogic(self.instate, self.name)
                
            


    class wire:
        def __init__(self,l):
            lst = l.split(';')
            self.slocked = int((lst[0]))
            self.elocked = int((lst[1]))

            self.inlocked = int(lst[2])
            self.outlocked = int(lst[3])
            self.iopin = int(lst[4])

            self.slog = int(lst[5])
            self.slop = int(lst[6])

            self.elog = int(lst[7])
            self.elop = int(lst[8])


    class inout:
        def __init__(self,l):
            lst = l.split(';')
            self.mode = int(lst[0])
            self.pinnum = int(lst[1])
            self.state = 0


    gatelst = []
    wirelst = []
    inoutlst = []
    for i in range(len(gates)):
        i = gate(gates[i],i)
        gatelst.append(i)
    for i in range(len(wires)):
        i = wire(wires[i])
        wirelst.append(i)
    for i in range(len(inouts)):
        i = inout(inouts[i])
        inoutlst.append(i)


    t = 0
    for ios in inoutlst:
        if ios.mode == 0:
            ios.state = instate[t]
            t += 1
        #print(ios.pinnum, ios.state)
    for frame in range(5):


        for w in wirelst:
            if w.inlocked == 1:
                w.state = inoutlst[w.iopin].state
            if w.slocked == 1:
                #print(gatelst[w.slog].name)
                w.state = gatelst[w.slog].outstate[w.slop-(gatelst[w.slog].innum)]

        for g in gatelst:
            for w in wirelst:
                if w.elocked == 1:
                    if w.elog == g.gid:
                        for i in range(g.innum + g.outnum):
                            s = list(g.instate)
                            s[w.elop] = str(w.state)
                            g.instate = ''.join(map(str, s))
            g.logic()
            #print(g.name)

        for ios in inoutlst:
            if ios.mode == 1:
                for w in wirelst:
                    if w.outlocked == 1:
                        if w.iopin == ios.pinnum:
                            ios.state = w.state

    final = ''
    for ios in inoutlst:
        if ios.mode == 1:
            final += str(ios.state)
    return final


#print(details('FBA'))