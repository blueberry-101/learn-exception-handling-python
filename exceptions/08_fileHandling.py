#ex-1 file handling
try:
    #suspesious code
    f = open("01_syntax.py",mode="r")

except Exception as e:
    print("something went wrong",e)

else:
    print("operations on the file is done")
    f.close()

print("rest of the code")

# confusion: why can't we close the file in the finally block
# In your code snippet, you're trying to close the file f before it's opened.
# 'f' was never initialized.
# answer :  you are trying to close the file which is not even opened as the 
# python intervpreter couldn't exceute the RHS side and throw and exception

'''
improved version
'''
try:
    # Suspicious code
    f = open("01_syntax.py", mode="r")
    
    # Operations on the file
    
except Exception as e:
    print("Something went wrong:", e)

else:
    print("Operations on the file are done")

finally:

    '''
    By placing f.close() in the finally block, you ensure that the file is closed regardless of whether the code in the try block raises an exception or not.
    
    Additionally, the if 'f' in locals(): condition checks if the variable f exists in the local namespace before attempting to close it
    '''

    if 'f' in locals():
        f.close()

print("Rest of the code")


#ex-2 db connection

