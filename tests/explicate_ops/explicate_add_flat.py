t3 = t0
t5 = t1
t8 = is_int(t3)
if t8:
    t9 = is_int(t5)
    if t9:
        t10 = project_int(t3)
        t11 = project_int(t5)
        t12 = t10 + t11
        t2 = inject_int(t12)
    else:
        t13 = is_bool(t5)
        if t13:
            t14 = project_int(t3)
            t15 = project_bool(t5)
            t16 = t14 + t15
            t2 = inject_int(t16)
        else:
            throw_type_error()
else:
    t17 = is_bool(t3)
    if t17:
        t18 = is_int(t5)
        if t18:
            t19 = project_bool(t3)
            t20 = project_int(t5)
            t21 = t19 + t20
            t2 = inject_int(t21)
        else:
            t22 = is_bool(t5)
            if t22:
                t23 = project_bool(t3)
                t24 = project_bool(t5)
                t25 = t23 + t24
                t2 = inject_int(t25)
            else:
                throw_type_error()
    else:
        t26 = is_int(t5)
        if t26:
            throw_type_error()
        t27 = is_int(t5)
        if t27:
            throw_type_error()
        else:
            t28 = is_big(t5)
            if t28:
                t29 = project_big(t3)
                t30 = project_big(t5)
                t31 = add(t29, t30)
                t2 = inject_big(t31)