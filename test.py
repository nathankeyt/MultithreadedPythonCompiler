#import "test_import.py" as a

print(a.a)

a.b = 1

def func2():
    print(a.b)
    print(a.a)

func2()
