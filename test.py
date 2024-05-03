y = 10

def add(a, b):
    return a + b

def inside(x):
    return lambda y: x + y

print(inside(10)(10))