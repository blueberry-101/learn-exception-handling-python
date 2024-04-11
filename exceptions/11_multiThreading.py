# if there are two threads and one thread throws error, will
# it stop another threads or not?

import threading 
from time import sleep
def sum():
    print("hello"+20)

def hello():

    for _ in range(5):
        sleep(0.5)
        print("hello")


t1 = threading.Thread(target=sum)
t2 = threading.Thread(target=hello)

t1.start()
t2.start()

# t1.join() working the same
t2.join()

for _ in range(5):
    sleep(0.5)
    print("main thread")



r"""
Exception in thread Thread-1 (sum):
Traceback (most recent call last):
  File "C:\PYTHON 3\lib\threading.py", line 1009, in _bootstrap_inner
    self.run()
  File "C:\PYTHON 3\lib\threading.py", line 946, in run
    self._target(*self._args, **self._kwargs)
  File "D:\PyPy\exceptions\11_multiThreading.py", line 8, in sum
    print("hello"+20)
TypeError: can only concatenate str (not "int") to str
hello
hello
hello
hello
hello
main thread
main thread
main thread
main thread
main thread
"""



'''

In the code snippet you provided, two threads `t1` and `t2` are created using the `threading.Thread` class. Each thread is assigned a target function to execute: `sum` for `t1` and `hello` for `t2`.

After creating the threads, they are started using the `start()` method. This initiates the execution of the target functions in separate threads, allowing them to run concurrently.

The `join()` method is then called on both `t1` and `t2`. The `join()` method blocks the calling thread (in this case, presumably the main thread) until the thread on which it is called (in this case, `t1` and `t2`) completes its execution. By calling `join()` on both threads, the main thread waits for both `t1` and `t2` to finish their execution before continuing.

So, the overall behavior of this code is to execute the `sum` and `hello` functions concurrently in separate threads, and the main thread waits for both of them to finish before proceeding further.

'''
# ANSWER IS NO!

# How to handle exception using funcion overriding in multithreading.

import threading 
from time import sleep

# defining custom exceptionhook fucntion

def custom_hook(*args):
    # print("something went wrong")
    # print(args[0])
    # print(args[1]) #outof range
    # print(args[2])
    print(args)
    """
    (_thread._ExceptHookArgs(exc_type=<class 'TypeError'>, exc_value=TypeError('can only concatenate str (not "int") to str'), exc_traceback=<traceback object at 0x0000019EC3BD98C0>, thread=<Thread(Thread-1 (sum), started 9900)>),)
    """

def sum():
    print("hello"+20)

def hello():

    for _ in range(5):
        sleep(0.5)
        print("hello")

# assigning custom except hook
threading.excepthook = custom_hook

t1 = threading.Thread(target=sum)
t2 = threading.Thread(target=hello)

t1.start()
t2.start()

# t1.join() working the same
t2.join()


for _ in range(5):
    sleep(0.5)
    print("main thread")
