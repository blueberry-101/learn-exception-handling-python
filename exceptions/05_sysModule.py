# Every exception like ZeroDivisionError or NameError are the
# classes which get called whenever the excetion occur

'''
Q. Suppose you want to know the class of exception and 
error message how will you know?

'''
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:")) 
try:
    result=num1/num2
    print(result)
except Exception as e:
    print(e.__class__) #gives exception name
    print(e) #gives excetion message

# print(Exception.__repr__)

'''
Q. Can you use sys module to print error name and error messsage?

'''
import sys
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:")) 
try:
    result=num1/num2
    print(result)
except :
    print(sys.exc_info())  # gives tuple (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000001C03C9938C0>)
    
    print(sys.exc_info()[0])  # Error name
    print(sys.exc_info()[1])  #Error message