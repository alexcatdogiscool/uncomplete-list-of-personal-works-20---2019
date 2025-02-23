
def all(fizz,buzz,length):
    def div(a, b):
        return (a % b == 0)
    for i in range(length):
        n = i+1

        if div(n,fizz) and div(n, buzz):
            print("FizzBuzz")
        elif div(n,fizz):
            print("Fizz")
        elif div(n,buzz):
            print("Buzz")
        else:
            print(n)


#all(3,5,100)


def all2(fizz,buzz,length):
    for i in range(length):
        n = i+1
        
        o = ""
        if n % 3 == 0:
            o += 'Fizz'
        if n % 5 == 0:
            o += "Buzz"

        if o == "":
            o = n
        
        print(o)

all2(3,5,100)