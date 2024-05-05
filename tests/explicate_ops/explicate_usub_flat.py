t4 = t2
t7 = is_int(t4)
if t7:
    t8 = project_int(t4)
    t9 = -t8
    t1 = inject_int(t9)
else:
    t10 = is_bool(t4)
    if t10:
        t11 = project_bool(t4)
        t12 = -t11
        t1 = inject_int(t12)
    else:
        throw_type_error()