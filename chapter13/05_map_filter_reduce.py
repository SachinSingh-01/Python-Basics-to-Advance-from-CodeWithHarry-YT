from functools import reduce

# List
l = [1, 2, 3, 4, 5]

# Map Example
square = lambda x: x * x
sqList = map(square, l)
print(list(sqList))  

# Filter Example
def even(n):
    return n % 2 == 0

onlyEven = filter(even, l)
print(list(onlyEven)) 

# Reduce Example
def sum(a, b):
    return a + b

mul=lambda x,y:x*y
print(reduce(sum,l))
print(reduce(mul,l)) 

