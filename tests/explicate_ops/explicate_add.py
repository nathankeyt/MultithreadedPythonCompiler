# a = b+c expands to
tmp0 = b # tmp var for let
tmp1 = c # tmp var for let
if(is_int(tmp0)):
    if(is_int(tmp1)): 
        a = inject_int(project_int(tmp0) + project_int(tmp1))
    else:
        if(is_bool(tmp1)):
            a = inject_int(project_int(tmp0) + project_bool(tmp1))
        else:
            throw_type_error()
else:
    if(is_bool(tmp0)):
        if(is_int(tmp1)):
            a = inject_int(project_bool(tmp0) + project_int(tmp1))
        else:
            if(is_bool(tmp1)):
                a = inject_int(project_bool(tmp0) + project_bool(tmp1))
            else:
                throw_type_error()
    else:
        if(is_int(tmp1)):
            throw_type_error()
        if(is_int(tmp1)):
            throw_type_error()
        elif(is_big(tmp1)):
            a = inject_big(add(project_big(tmp0), project_big(tmp1)))
