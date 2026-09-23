#expression = input("equation:")
#result = eval(expression)
#print(result)

def add(x,y):return(x + y)
def sub(x,y):return(x - y)
def mult(x,y):return(x * y)
def div(x,y):
    if y == 0:print("zero error")
    else:return x/y



#function adds X and y

while True:
    d = input("decisionoperation use -,+,/,*:")
    a,b = int(input("first number:").strip(),input("second number:").strip())
    if d == "/":div(a,b)
    if d == "+":add(a,b)
    if d == "-":sub(a,b)
    if d == "*":mult(a,b)
    else:
        if input("you done if yes type yes") == "yes":break
