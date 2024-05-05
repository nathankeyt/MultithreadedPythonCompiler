t131 = t2
t134 = is_int(t131)
if t134:
    t135 = project_int(t131)
    t3 = inject_int(t135)
else:
    t136 = is_bool(t131)
    if t136:
        t137 = project_bool(t131)
        t3 = inject_int(t137)
    else:
        throw_type_error()