t742 = t6
t745 = is_int(t742)
if t745:
    t746 = project_int(t742)
    t7 = inject_int(t746)
else:
    t747 = is_bool(t742)
    if t747:
        t748 = project_bool(t742)
        t7 = inject_int(t748)
    else:
        throw_type_error()