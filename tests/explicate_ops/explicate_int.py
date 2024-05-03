# a = int(b) expands to
tmp0 = b # tmp var for let
if(is_int(tmp0)):
    a = inject_int(project_int(tmp0))
else:
    if (is_bool(tmp0)):
        a = inject_int(project_bool(tmp0))
    else:
        throw_type_error()
