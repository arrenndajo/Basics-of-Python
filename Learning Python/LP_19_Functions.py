# There are 3 types of Functions in Python: 
# 1. In-Built Funtion
# 2. Module Function
# 3. User-Defined Function

# 1. In-Built Funtion
# int(), str(), bool()

# 2. Module Function
# math is a module, in which many functions are present
import math
print(dir(math))

# we can pick specific function from math module and use it
from math import sqrt
print(sqrt(16))

# this imports all the functions from the module 
from math import *

# 3. User-Defined Function
def print_sum(first, second):
    print(first + second)
print_sum(1, 2) # 1+2=3, 3 will be the output

def print_sum(first, second=4): # 1+4=5, 5 is the output
    print(first + second)
print_sum(1)

def print_sum(first, second=3): # here, 3 will be taken
    print(first + second)
print_sum(1, 5) # 1+5=6, 6 is the output
