#expression = input("equation:")
#result = eval(expression)
#print(result)

def add(x,y):print("\n",x + y,"\n")
def sub(x,y):print("\n",x - y,"\n")
def mult(x,y):print("\n",x * y,"\n")
def div(x,y):
    if y == 0:print("zero error")
    else:print("\n",x/y,"\n")



print("welcome user")

while True:
    print("what do you want to do")
    d = input("(a)add,(s)subtract,(m)multiply,(d)divide,(q)quit")
    if d == 'd':a,b = int(input("first number:").strip()),int(input("second number:").strip());div(a,b)
    elif d == 'a':a,b = int(input("first number:").strip()),int(input("second number:").strip());add(a,b)
    elif d == 's':a,b = int(input("first number:").strip()),int(input("second number:").strip());sub(a,b)
    elif d == 'm':a,b = int(input("first number:").strip()),int(input("second number:").strip());mult(a,b)
    elif d == 'q':
        if input("you done if yes type yes") == "yes":break
    else:
        print("bro type a,s,m,d or q")
