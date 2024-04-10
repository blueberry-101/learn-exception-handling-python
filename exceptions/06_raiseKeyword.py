# raise keyword is Used to forcefully call any excetion at any particular condition

try:
    age = int(input("enter your age:"))
    if age<0:
        raise ValueError
    else:
        print("Your age is valid")
except Exception as e:
    print("something went wrong->",e)

'''
output:

enter your age:-32
something went wrong-> 

'''

#                                 *********


try:
    age = int(input("enter your age:"))
    if age<0:
        raise ValueError("age can't be negative")
    else:
        print("Your age is valid")
except Exception as e:
    print(e)

'''
output: 

enter your age:-23     
age can't be negative

'''

