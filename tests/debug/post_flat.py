t0 = inject_int(1)
t1 = inject_int(100)
t2 = t0 != t1
t3 = int(t2)
t4 = is_true(t3)
while t4:
    t5 = inject_int(1)
    t0 = t0 + t5
    t6 = t0 and t1
    print(t6)
    t2 = t0 != t1
    t3 = int(t2)
    t4 = is_true(t3)