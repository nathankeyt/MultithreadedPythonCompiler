#import "test_import.py" as t

t.a = 1
print(t.a)

t.b = 1

def func2():
    print(t.b)

func2()
