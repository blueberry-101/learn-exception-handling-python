'''
can you change the definition of the function.
which function?
the function who is responsible for throwing traceback error.
the new definition will only print those three (class,message,object) and never stop the execution.
'''

def sum():
    print(1+"hello")

sum()

r'''

  File "D:\PyPy\exceptions\10_redefine.py", line 11, in <module>
    sum()
  File "D:\PyPy\exceptions\10_redefine.py", line 9, in sum      
    print(1+"hello")
TypeError: unsupported operand type(s) for +: 'int' and 'str'  

'''

# SOLUTION v1.0

import sys
def traceback_function(sys_type,sys_message,sys_obj):
    print("something went wrong")

sys.excepthook  = traceback_function

def sum():
    print(1+"hello")

sum()


'''

something went wrong

'''

# SOLUTION v1.1

import sys
def traceback_function(sys_type,sys_message,sys_obj):
    print("something went wrong")
    print(sys_type)
    print(sys_message)
    print(sys_obj)

sys.excepthook  = traceback_function

def sum():
    print(1+"hello")

sum()


'''

something went wrong
<class 'TypeError'>
unsupported operand type(s) for +: 'int' and 'str'
<traceback object at 0x0000018984926980>

'''