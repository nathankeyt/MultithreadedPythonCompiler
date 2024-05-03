t1073 = t12
t1075 = t18
t1078 = is_int(t1073)
if t1078:
    t1079 = is_int(t1075)
    if t1079:
        t1080 = project_int(t1073)
        t1081 = project_int(t1075)
        t1082 = t1080 != t1081
        t19 = inject_bool(t1082)
    else:
        t1083 = is_bool(t1075)
        if t1083:
            t1084 = project_int(t1073)
            t1085 = project_bool(t1075)
            t1086 = t1084 != t1085
            t19 = inject_bool(t1086)
        else:
            t1087 = project_int(t1073)
            t1088 = project_big(t1075)
            t1089 = t1087 != t1088
            t19 = inject_bool(t1089)
else:
    t1090 = is_bool(t1073)
    if t1090:
        t1091 = is_int(t1075)
        if t1091:
            t1092 = project_bool(t1073)
            t1093 = project_int(t1075)
            t1094 = t1092 != t1093
            t19 = inject_bool(t1094)
        else:
            t1095 = is_bool(t1075)
            if t1095:
                t1096 = project_bool(t1073)
                t1097 = project_bool(t1075)
                t1098 = t1096 != t1097
                t19 = inject_bool(t1098)
            else:
                t1099 = project_bool(t1073)
                t1100 = project_big(t1075)
                t1101 = t1099 != t1100
                t19 = inject_bool(t1101)
    else:
        t1102 = is_int(t1075)
        if t1102:
            t1103 = project_big(t1073)
            t1104 = project_int(t1075)
            t1105 = t1103 != t1104
            t19 = inject_bool(t1105)
        else:
            t1106 = is_bool(t1075)
            if t1106:
                t1107 = project_big(t1073)
                t1108 = project_bool(t1075)
                t1109 = t1107 != t1108
                t19 = inject_bool(t1109)
            else:
                t1110 = project_big(t1073)
                t1111 = project_big(t1075)
                t1112 = not_equal(t1110, t1111)
                t19 = inject_bool(t1112)