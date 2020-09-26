def inner(i):
    return i + 1

def outer_1(n):
    x = 0
    for i in range(n):
        x = inner(x)

def outer_2(n):
    x = 0
    for i in range(n):
        x = x + 1
