t128 = t3
t130 = t14
t133 = is_int(t128)
if t133:
    t134 = is_int(t130)
    if t134:
        t135 = project_int(t128)
        t136 = project_int(t130)
        t137 = t135 + t136
        t3 = inject_int(t137)
    else:
        t138 = is_bool(t130)
        if t138:
            t139 = project_int(t128)
            t140 = project_bool(t130)
            t141 = t139 + t140
            t3 = inject_int(t141)
        else:
            throw_type_error()
else:
    t142 = is_bool(t128)
    if t142:
        t143 = is_int(t130)
        if t143:
            t144 = project_bool(t128)
            t145 = project_int(t130)
            t146 = t144 + t145
            t3 = inject_int(t146)
        else:
            t147 = is_bool(t130)
            if t147:
                t148 = project_bool(t128)
                t149 = project_bool(t130)
                t150 = t148 + t149
                t3 = inject_int(t150)
            else:
                throw_type_error()
    else:
        t151 = is_int(t130)
        if t151:
            throw_type_error()
        t152 = is_int(t130)
        if t152:
            throw_type_error()
        else:
            t153 = is_big(t130)
            if t153:
                t154 = project_big(t128)
                t155 = project_big(t130)
                t156 = add(t154, t155)
                t3 = inject_big(t156)