u =int(input("Enter 1st no: "))
y =int(input("Enter 2nd no: "))
o =int(input("Choose any option 1=add 2=subtract 3=multiply 4=divide"))
def add(u, y):
    print(u+y)
def subtract(u, y):
    print(u-y)
def multiply(u, y):
    print(u*y)
def divide(u, y):
    print(u//y)
if o==1:
    add(u,y)
if o==2:
    subtract(u,y)
if o==3:
    multiply(u,y)
if o==4:
    divide(u,y)

    