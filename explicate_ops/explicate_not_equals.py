# a = b != c expands to
t0 = b # tmp var for let
t1 = c # tmp var for let

if(is_int(t0)):
    if(is_int(t1)):
        a = inject_bool(project_int(t0) != project_int(t1))
    else:
        if(is_bool(t1)):
            a = inject_bool(project_int(t0) != project_bool(t1))
        else:
            a = inject_bool(project_int(t0) != project_big(t1))
else:
    if(is_bool(t0)):
        if(is_int(t1)):
            a = inject_bool(project_bool(t0) != project_int(t1))
        else:
            if(is_bool(t1)):
                a = inject_bool(project_bool(t0) != project_bool(t1))
            else:
                a = inject_bool(project_bool(t0) != project_big(t1))
    else:
        if(is_int(t1)):
            a = inject_bool(project_big(t0) != project_int(t1))
        else:
            if(is_bool(t1)):
                a = inject_bool(project_big(t0) != project_bool(t1))
            else:
                a = inject_bool(not_equal(project_big(t0), project_big(t1)))

