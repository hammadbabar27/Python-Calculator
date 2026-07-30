#calculator using functions

def addition(a,b):
    print(f"Addition of {a} & {b} is: {a+b}")
    return a+b

def subtraction(a,b):
    print(f"Addition of {a} & {b} is: {a-b}")
    return a-b

def mult(a,b):
    print(f"Addition of {a} & {b} is: {a*b}")
    return a*b

def divi(a,b):
    print(f"Addition of {a} & {b} is: {a/b}")
    return a/b

while True:
    def menu():
        print("Enter 1 For Addition")
        print("Enter 2 For Subtraction")
        print("Enter 3 For Multiplication")
        print("Enter 4 For Division")
        print("Enter 9 for Exit")
    
    menu()

    m = int(input("\n Enter Choice Here: "))

    if m == 9:
        break

    elif m not in [1,2,3,4]: 
            print("Invalid Choice. Try Again! \n")
            continue
    
    n1 = float(input("\n Enter 1st Number: "))
    n2 = float(input("\n Enter 2nd Number: "))

    if m == 1:
        addition(n1, n2)
        print("\n")

    elif m == 2:
        subtraction(n1, n2)
        print("\n")

    elif m == 3:
        mult(n1, n2)
        print("\n")

    elif m == 4:
        divi(n1, n2)
        print("\n")

