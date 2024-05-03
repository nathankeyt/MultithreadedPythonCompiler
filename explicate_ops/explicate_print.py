tmp0 = b # tmp var for let
if(is_int(tmp0)):
    a = project_int(tmp0)
else:
    if(is_bool(tmp0)):
        a = project_bool(tmp0)
    else:
        a = project_big(tmp0)
