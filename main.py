#expression = input("equation:")
#result = eval(expression)
#print(result)

def add(x,y):print(x + y)
def sub(x,y):print(x - y)
def mult(x,y):print(x * y)
def div(x,y):
    if y == 0:print("zero error")
    else:print(x/y)



print("welcome user")

while True:
    print("what do you want to do")
    d,a,b, = input("(a)add,(s)subtract,(m)multiply,(d)divide"),int(input("first number:").strip()),int(input("second number:").strip())
    if d == "d":div(a,b)
    if d == "a":add(a,b)
    if d == "s":sub(a,b)
    if d == "m":mult(a,b)
    else:
        if input("you done if yes type yes") == "yes":break
