num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
try:
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("error occurred")

