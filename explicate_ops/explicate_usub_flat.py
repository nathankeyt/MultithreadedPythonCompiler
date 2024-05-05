t172 = t16
t175 = is_int(t172)
if t175:
    t176 = project_int(t172)
    t177 = -t176
    t17 = inject_int(t177)
else:
    t178 = is_bool(t172)
    if t178:
        t179 = project_bool(t172)
        t180 = -t179
        t17 = inject_int(t180)
    else:
        throw_type_error()