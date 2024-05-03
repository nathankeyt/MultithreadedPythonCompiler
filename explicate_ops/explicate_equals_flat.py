t116 = t2
t118 = t43
t121 = is_int(t116)
if t121:
    t122 = is_int(t118)
    if t122:
        t123 = project_int(t116)
        t124 = project_int(t118)
        t125 = t123 == t124
        t44 = inject_bool(t125)
    else:
        t126 = is_bool(t118)
        if t126:
            t127 = project_int(t116)
            t128 = project_bool(t118)
            t129 = t127 == t128
            t44 = inject_bool(t129)
        else:
            t130 = project_int(t116)
            t131 = project_big(t118)
            t132 = t130 == t131
            t44 = inject_bool(t132)
else:
    t133 = is_bool(t116)
    if t133:
        t134 = is_int(t118)
        if t134:
            t135 = project_bool(t116)
            t136 = project_int(t118)
            t137 = t135 == t136
            t44 = inject_bool(t137)
        else:
            t138 = is_bool(t118)
            if t138:
                t139 = project_bool(t116)
                t140 = project_bool(t118)
                t141 = t139 == t140
                t44 = inject_bool(t141)
            else:
                t142 = project_bool(t116)
                t143 = project_big(t118)
                t144 = t142 == t143
                t44 = inject_bool(t144)
    else:
        t145 = is_int(t118)
        if t145:
            t146 = project_big(t116)
            t147 = project_int(t118)
            t148 = t146 == t147
            t44 = inject_bool(t148)
        else:
            t149 = is_bool(t118)
            if t149:
                t150 = project_big(t116)
                t151 = project_bool(t118)
                t152 = t150 == t151
                t44 = inject_bool(t152)
            else:
                t153 = project_big(t116)
                t154 = project_big(t118)
                t155 = equal(t153, t154)
                t44 = inject_bool(t155)