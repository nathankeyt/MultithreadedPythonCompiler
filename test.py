#import "test_import.py" as im

a = 3
im.a = 8

def func(a):
    print(a)
    print(b)
    print(im.a)

b = 2

func(im.b)