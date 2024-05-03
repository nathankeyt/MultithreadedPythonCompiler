t16 = t2
t18 = t3
t21 = is_int(t16)
if t21:
    t22 = is_int(t18)
    if t22:
        t23 = project_int(t16)
        t24 = project_int(t18)
        t25 = t23 + t24
        t4 = inject_int(t25)
    else:
        t26 = is_bool(t18)
        if t26:
            t27 = project_int(t16)
            t28 = project_bool(t18)
            t29 = t27 + t28
            t4 = inject_int(t29)
        else:
            throw_type_error()
else:
    t30 = is_bool(t16)
    if t30:
        t31 = is_int(t18)
        if t31:
            t32 = project_bool(t16)
            t33 = project_int(t18)
            t34 = t32 + t33
            t4 = inject_int(t34)
        else:
            t35 = is_bool(t18)
            if t35:
                t36 = project_bool(t16)
                t37 = project_bool(t18)
                t38 = t36 + t37
                t4 = inject_int(t38)
            else:
                throw_type_error()
    else:
        t39 = is_int(t18)
        if t39:
            throw_type_error()
        t40 = is_int(t18)
        if t40:
            throw_type_error()
        else:
            t41 = is_big(t18)
            if t41:
                t42 = project_big(t16)
                t43 = project_big(t18)
                t44 = add(t42, t43)
                t4 = inject_big(t44)