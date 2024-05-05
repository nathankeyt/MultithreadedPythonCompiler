t4 = t0
t6 = t1
t9 = is_int(t4)
if t9:
    t10 = is_int(t6)
    if t10:
        t11 = project_int(t4)
        t12 = project_int(t6)
        t13 = t11 == t12
        t2 = inject_bool(t13)
    else:
        t14 = is_bool(t6)
        if t14:
            t15 = project_int(t4)
            t16 = project_bool(t6)
            t17 = t15 == t16
            t2 = inject_bool(t17)
        else:
            t18 = project_int(t4)
            t19 = project_big(t6)
            t20 = t18 == t19
            t2 = inject_bool(t20)
else:
    t21 = is_bool(t4)
    if t21:
        t22 = is_int(t6)
        if t22:
            t23 = project_bool(t4)
            t24 = project_int(t6)
            t25 = t23 == t24
            t2 = inject_bool(t25)
        else:
            t26 = is_bool(t6)
            if t26:
                t27 = project_bool(t4)
                t28 = project_bool(t6)
                t29 = t27 == t28
                t2 = inject_bool(t29)
            else:
                t30 = project_bool(t4)
                t31 = project_big(t6)
                t32 = t30 == t31
                t2 = inject_bool(t32)
    else:
        t33 = is_int(t6)
        if t33:
            t34 = project_big(t4)
            t35 = project_int(t6)
            t36 = t34 == t35
            t2 = inject_bool(t36)
        else:
            t37 = is_bool(t6)
            if t37:
                t38 = project_big(t4)
                t39 = project_bool(t6)
                t40 = t38 == t39
                t2 = inject_bool(t40)
            else:
                t41 = project_big(t4)
                t42 = project_big(t6)
                t43 = equal(t41, t42)
                t2 = inject_bool(t43)