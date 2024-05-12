# 1
def timer():
    def inner():
        print('time started')

        print('time ended')
    return inner

# timer()()

def get_factorial():
    print('factorial aha\n')

get_factorial()

# 2
def timer(func):
    def inner():
        print('time started')
        # print(func)
        func()

        print('time ended\n')
    return inner

@timer
def get_factorial():
    print('factorial aha')

get_factorial()

# vejailla way to decorate
# timer(get_factorial)()

# 3
import math
import time
def timer(func):
    def inner(*args,**kwargs):
        start=time.time()
        print('time started')
        # print(func)
        func(*args,**kwargs)

        print('time ended')
        end=time.time()
        print(f'time has taken : {end-start}')
    return inner

@timer
def get_factorial(n):
    print('factorial aha')
    result=math.factorial(n)
    print(f'factorial of {n} is {result}')

get_factorial(5)