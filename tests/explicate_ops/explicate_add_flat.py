t54 = t0
t56 = t5
t59 = is_int(t54)
if t59:
    t60 = is_int(t56)
    if t60:
        t61 = project_int(t54)
        t62 = project_int(t56)
        t63 = t61 + t62
        t0 = inject_int(t63)
    else:
        t64 = is_bool(t56)
        if t64:
            t65 = project_int(t54)
            t66 = project_bool(t56)
            t67 = t65 + t66
            t0 = inject_int(t67)
        else:
            throw_type_error()
else:
    t68 = is_bool(t54)
    if t68:
        t69 = is_int(t56)
        if t69:
            t70 = project_bool(t54)
            t71 = project_int(t56)
            t72 = t70 + t71
            t0 = inject_int(t72)
        else:
            t73 = is_bool(t56)
            if t73:
                t74 = project_bool(t54)
                t75 = project_bool(t56)
                t76 = t74 + t75
                t0 = inject_int(t76)
            else:
                throw_type_error()
    else:
        t77 = is_int(t56)
        if t77:
            throw_type_error()
        t78 = is_int(t56)
        if t78:
            throw_type_error()
        else:
            t79 = is_big(t56)
            if t79:
                t80 = project_big(t54)
                t81 = project_big(t56)
                t82 = add(t80, t81)
                t0 = inject_big(t82)