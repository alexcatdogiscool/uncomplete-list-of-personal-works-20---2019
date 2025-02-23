import matplotlib.pyplot as plt

f = open('data.txt','r')
datas = f.read()
f.close()

data = []
datas = datas.split('\n')
del datas[-1]
print(len(datas))
for i in range(len(datas)-3):
    val = (float(datas[i]) + float(datas[i+1]) + float(datas[i+2]) + float(datas[i+3]))/2
    data.append(val)


plt.plot(data)
plt.show()