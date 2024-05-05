t0 = inject_int(1)
t2 = t0
t5 = is_int(t2)
if t5:
    t6 = project_int(t2)
    t7 = -t6
    t1 = inject_int(t7)
else:
    t8 = is_bool(t2)
    if t8:
        t9 = project_bool(t2)
        t10 = -t9
        t1 = inject_int(t10)
    else:
        throw_type_error()
print(t1)