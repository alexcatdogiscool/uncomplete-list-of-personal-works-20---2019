

def winge(x, s):
    y = {}
    ks = [k for k in x.keys() if k in s]
    print(ks)
    for k in ks:
        print(k)
        for c in x[k]:
            print(c)
            if c in y:
                y[c].append(k)
            else:
                y[c] = [k]
    print(sorted(y.items()))
