i = 0
while True:
    s = ""
    if i % 3 == 0:
        s += "fizz"
    if i % 5 == 0:
        s += "buzz"
    if s == "":
        s += str(i)
    print(s)
    i += 1