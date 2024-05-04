t157 = t1
t159 = t8
t162 = is_int(t157)
if t162:
    t163 = is_int(t159)
    if t163:
        t164 = project_int(t157)
        t165 = project_int(t159)
        t166 = t164 != t165
        t9 = inject_bool(t166)
    else:
        t167 = is_bool(t159)
        if t167:
            t168 = project_int(t157)
            t169 = project_bool(t159)
            t170 = t168 != t169
            t9 = inject_bool(t170)
        else:
            t171 = project_int(t157)
            t172 = project_big(t159)
            t173 = t171 != t172
            t9 = inject_bool(t173)
else:
    t174 = is_bool(t157)
    if t174:
        t175 = is_int(t159)
        if t175:
            t176 = project_bool(t157)
            t177 = project_int(t159)
            t178 = t176 != t177
            t9 = inject_bool(t178)
        else:
            t179 = is_bool(t159)
            if t179:
                t180 = project_bool(t157)
                t181 = project_bool(t159)
                t182 = t180 != t181
                t9 = inject_bool(t182)
            else:
                t183 = project_bool(t157)
                t184 = project_big(t159)
                t185 = t183 != t184
                t9 = inject_bool(t185)
    else:
        t186 = is_int(t159)
        if t186:
            t187 = project_big(t157)
            t188 = project_int(t159)
            t189 = t187 != t188
            t9 = inject_bool(t189)
        else:
            t190 = is_bool(t159)
            if t190:
                t191 = project_big(t157)
                t192 = project_bool(t159)
                t193 = t191 != t192
                t9 = inject_bool(t193)
            else:
                t194 = project_big(t157)
                t195 = project_big(t159)
                t196 = not_equal(t194, t195)
                t9 = inject_bool(t196)