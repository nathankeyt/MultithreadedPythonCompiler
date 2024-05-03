b = 10
c = 2
e = 11

def func(a):

    c = 10
    while (a != 0):
        c = c + 1
        print(a)
        if (a == 10):
            b = 10
            while (b != 0):
                b = b + -1
                c = 20
            a = a + -1
        else:
            a = a + -1

    return a

def func2(a):

    c = 10
    while (a != 0):
        c = c + 1
        print(a)
        if (a == 10):
            b = 10
            while (b != 0):
                b = b + -1
                c = 20
            a = a + -1
        else:
            a = a + -1

    return a


def func3(a):

    c = 10
    while (a != 0):
        c = c + 1
        print(a)
        if (a == 10):
            b = 10
            while (b != 0):
                b = b + -1
                c = 20
            a = a + -1
        else:
            a = a + -1

    return a

print(func(10))
print(func2(5))
print(func3(5))