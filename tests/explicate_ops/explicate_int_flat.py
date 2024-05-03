t9 = t1
t12 = is_int(t9)
if t12:
    t13 = project_int(t9)
    t2 = inject_int(t13)
else:
    t14 = is_bool(t9)
    if t14:
        t15 = project_bool(t9)
        t2 = inject_int(t15)
    else:
        throw_type_error()