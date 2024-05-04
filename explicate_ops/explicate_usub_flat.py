t90 = t12
t93 = is_int(t90)
if t93:
    t94 = project_int(t90)
    t95 = -t94
    t13 = inject_int(t95)
else:
    t96 = is_bool(t90)
    if t96:
        t97 = project_bool(t90)
        t98 = -t97
        t13 = inject_int(t98)
    else:
        throw_type_error()