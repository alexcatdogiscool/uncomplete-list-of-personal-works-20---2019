from selenium import webdriver
import string
import time
digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return "a"#digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[(x+10) % base])
        x = x // base

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)



def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]



option = webdriver.ChromeOptions()
option.add_argument("-incognito")
browser = webdriver.Chrome(executable_path='chromedriver.exe', options=option)


link = "https://prnt.sc/"
addLn = 120
addL = "aa"
addN = 0
addNs = ""

for i in range(100):
    addNs = "0"*(4-len(str(addN))) + str(addN)
    print(link + addL + addNs)
    browser.get(link+addL+addNs)
    addLn += 1
    
    addL = ""
    for l in numberToBase(addLn, 26):
        addL += chr(l+97)
    if len(addL) == 1:
        addL = "a" + addL
    if addL == "zz":
        addLn = -1
        addN += 1
    
    time.sleep(1)
    
    






