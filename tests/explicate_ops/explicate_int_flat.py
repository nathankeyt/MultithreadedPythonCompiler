t957 = t5
t960 = is_int(t957)
if t960:
    t961 = project_int(t957)
    t6 = inject_int(t961)
else:
    t962 = is_bool(t957)
    if t962:
        t963 = project_bool(t957)
        t6 = inject_int(t963)
    else:
        throw_type_error()