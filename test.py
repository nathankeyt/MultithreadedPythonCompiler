#import "test_import.py" as im

im.do_something()

a = 3
im.a = 8

def func(a):
    print(a)
    print(b)
    print(im.a)

b = 2

func(im.b)
im.do_something()