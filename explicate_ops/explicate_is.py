# a = b+c expands to
tmp0 = b # tmp var for let
tmp1 = c # tmp var for let
# if(is_int(t0)):
#     if(is_int(t1)):
#         a = inject_bool(project_int(t0) is project_int(t1))
#     elif(is_bool(t1)):
#         a = inject_bool(project_int(t0) is project_bool(t1))
#     elif(is_big(t1)):
#         a = inject_bool(project_int(t0) is project_big(t1))
# elif(is_bool(t0)):
#     if(is_int(t1)):
#         a = inject_bool(project_bool(t0) is project_int(t1))
#     elif(is_bool(t1)):
#         a = inject_bool(project_bool(t0) is project_bool(t1))
#     elif(is_big(t1)):
#         a = inject_bool(project_bool(t0) is project_big(t1))
# elif(is_big(t0)):
#     if(is_int(t1)):
#         a = inject_bool(project_big(t0) is project_int(t1))
#     elif(is_bool(t1)):
#         a = inject_bool(project_big(t0) is project_bool(t1))
#     elif(is_big(t1)):
#         a = inject_bool(project_big(t0) is project_big(t1))
a = inject_bool(tmp0 == tmp1)