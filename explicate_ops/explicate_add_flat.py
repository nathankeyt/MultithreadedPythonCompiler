t1044 = t12
t1046 = t33
t1049 = is_int(t1044)
if t1049:
    t1050 = is_int(t1046)
    if t1050:
        t1051 = project_int(t1044)
        t1052 = project_int(t1046)
        t1053 = t1051 + t1052
        t12 = inject_int(t1053)
    else:
        t1054 = is_bool(t1046)
        if t1054:
            t1055 = project_int(t1044)
            t1056 = project_bool(t1046)
            t1057 = t1055 + t1056
            t12 = inject_int(t1057)
        else:
            throw_type_error()
else:
    t1058 = is_bool(t1044)
    if t1058:
        t1059 = is_int(t1046)
        if t1059:
            t1060 = project_bool(t1044)
            t1061 = project_int(t1046)
            t1062 = t1060 + t1061
            t12 = inject_int(t1062)
        else:
            t1063 = is_bool(t1046)
            if t1063:
                t1064 = project_bool(t1044)
                t1065 = project_bool(t1046)
                t1066 = t1064 + t1065
                t12 = inject_int(t1066)
            else:
                throw_type_error()
    else:
        t1067 = is_int(t1046)
        if t1067:
            throw_type_error()
        t1068 = is_int(t1046)
        if t1068:
            throw_type_error()
        else:
            t1069 = is_big(t1046)
            if t1069:
                t1070 = project_big(t1044)
                t1071 = project_big(t1046)
                t1072 = add(t1070, t1071)
                t12 = inject_big(t1072)