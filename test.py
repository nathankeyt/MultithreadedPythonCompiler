#import "test_import.py" as t

print(t.a)

t.b = 1

def func2():
    print(t.b)
    print(t.a)

func2()
