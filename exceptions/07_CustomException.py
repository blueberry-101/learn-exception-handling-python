# write a python program to create FiveDivisionError Exception class

class FiveDivisionError(Exception):
    def __init__(self):
        print("cannot divide by 5")
    

try:
    n1 = int(input("enter first number:"))
    n2 = int(input("enter second number:"))

    if n2==5:
        raise FiveDivisionError
    else:
        print(n1/n2)

except (FiveDivisionError,ZeroDivisionError) as e:

    print("something went wrong->",e)

