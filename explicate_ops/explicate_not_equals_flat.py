t210 = t6
t212 = t8
t215 = is_int(t210)
if t215:
    t216 = is_int(t212)
    if t216:
        t217 = project_int(t210)
        t218 = project_int(t212)
        t219 = t217 != t218
        t9 = inject_bool(t219)
    else:
        t220 = is_bool(t212)
        if t220:
            t221 = project_int(t210)
            t222 = project_bool(t212)
            t223 = t221 != t222
            t9 = inject_bool(t223)
        else:
            t224 = project_int(t210)
            t225 = project_big(t212)
            t226 = t224 != t225
            t9 = inject_bool(t226)
else:
    t227 = is_bool(t210)
    if t227:
        t228 = is_int(t212)
        if t228:
            t229 = project_bool(t210)
            t230 = project_int(t212)
            t231 = t229 != t230
            t9 = inject_bool(t231)
        else:
            t232 = is_bool(t212)
            if t232:
                t233 = project_bool(t210)
                t234 = project_bool(t212)
                t235 = t233 != t234
                t9 = inject_bool(t235)
            else:
                t236 = project_bool(t210)
                t237 = project_big(t212)
                t238 = t236 != t237
                t9 = inject_bool(t238)
    else:
        t239 = is_int(t212)
        if t239:
            t240 = project_big(t210)
            t241 = project_int(t212)
            t242 = t240 != t241
            t9 = inject_bool(t242)
        else:
            t243 = is_bool(t212)
            if t243:
                t244 = project_big(t210)
                t245 = project_bool(t212)
                t246 = t244 != t245
                t9 = inject_bool(t246)
            else:
                t247 = project_big(t210)
                t248 = project_big(t212)
                t249 = not_equal(t247, t248)
                t9 = inject_bool(t249)