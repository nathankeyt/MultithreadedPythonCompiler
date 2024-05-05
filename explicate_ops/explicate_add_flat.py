t181 = t6
t183 = t17
t186 = is_int(t181)
if t186:
    t187 = is_int(t183)
    if t187:
        t188 = project_int(t181)
        t189 = project_int(t183)
        t190 = t188 + t189
        t6 = inject_int(t190)
    else:
        t191 = is_bool(t183)
        if t191:
            t192 = project_int(t181)
            t193 = project_bool(t183)
            t194 = t192 + t193
            t6 = inject_int(t194)
        else:
            throw_type_error()
else:
    t195 = is_bool(t181)
    if t195:
        t196 = is_int(t183)
        if t196:
            t197 = project_bool(t181)
            t198 = project_int(t183)
            t199 = t197 + t198
            t6 = inject_int(t199)
        else:
            t200 = is_bool(t183)
            if t200:
                t201 = project_bool(t181)
                t202 = project_bool(t183)
                t203 = t201 + t202
                t6 = inject_int(t203)
            else:
                throw_type_error()
    else:
        t204 = is_int(t183)
        if t204:
            throw_type_error()
        t205 = is_int(t183)
        if t205:
            throw_type_error()
        else:
            t206 = is_big(t183)
            if t206:
                t207 = project_big(t181)
                t208 = project_big(t183)
                t209 = add(t207, t208)
                t6 = inject_big(t209)