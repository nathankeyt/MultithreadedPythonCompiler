#import "./import_files/test_import.py" as im
#import "./import_files/nested_import.py" as ne

im.do_something()

a = 3
im.a = 8

def func(a):
    e = 1
    c = 2

    while (c != 1):
        if (c == 2):
            c = c + -1
        else:
            c = c + -2
    
    print(e)
    print(c)
    print(a)
    print(b)
    print(im.a)
    print(im.ne.b)

b = 2

func(im.b)
im.do_something()

im.ne.do_something()

im.ne.a = 200

im.ne.do_something()

ne.do_something()