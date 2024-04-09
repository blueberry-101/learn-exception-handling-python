num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:")) 
try:
    result=num1/num2
    print(resul)
except (ZeroDivisionError,NameError):
    print("error occurred")

#  OR

try:
    result=num1/num2
    print(resul)
except (ZeroDivisionError):
    print("zero error occurred")

except NameError:
    print("name error occured")


# Assign error message to variable "e" 
try:
    result=num1/num2
    print(resul)
except (ZeroDivisionError,NameError) as e:
    print(e)

# when you don't know what error could occur

try:
    result=num1/num2
    print(result)
except Exception as e:
    print(e)