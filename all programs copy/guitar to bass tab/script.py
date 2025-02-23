import numpy as np







def program(filename):

    file = open(filename, 'r')
    data = file.read()
    
    data = data.splitlines()
    

    n_rows = len(data)
    n_cols = len(data[0])

    for row in range(2):
        for col in range(n_cols):
            value = data[row][col]
            value_next = data[row][col+1]
            if value != '-':
                if value_next == '-':
                    if row == 0:
                        data[row+1][col] = str(int(value) + 5)
                    
                    if row == 1:
                        data[row+1][col] = str(int(value) + 4)
                else:
                    

    return data



print(program('guitar.txt'))