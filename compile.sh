python3 compiler.py test.py test2.py

gcc -m32 -g test2.s runtime/libpyyruntime.a -lm -o test2

./test2

gcc -m32 -g test.s runtime/libpyyruntime.a -lm -o test

./test