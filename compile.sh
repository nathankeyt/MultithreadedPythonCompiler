python3 compiler.py test.py

gcc -m32 -g test.s runtime/libpyyruntime.a -lm -o test

./test