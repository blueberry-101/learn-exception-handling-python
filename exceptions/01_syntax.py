'''What is an exception?
 An exception is an event which occures during the execution
of program that disrupts normal flow of program.

you cannot handle error : like syntax error
but you can handle exceptions '''

try:
    #code containing the suspisious code in which 
    pass
except Exception:
    #code to handle exception
    pass
else:
    # code to run if exception doesnt run
    pass

finally:
    #code to run always. either exception occur not not occur
    # file code, or DB connection close.
    pass

