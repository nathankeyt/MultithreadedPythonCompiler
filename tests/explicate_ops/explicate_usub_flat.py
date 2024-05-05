t118 = t9
t121 = is_int(t118)
if t121:
    t122 = project_int(t118)
    t123 = -t122
    t10 = inject_int(t123)
else:
    t124 = is_bool(t118)
    if t124:
        t125 = project_bool(t118)
        t126 = -t125
        t10 = inject_int(t126)
    else:
        throw_type_error()