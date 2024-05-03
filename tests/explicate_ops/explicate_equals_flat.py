t56 = t4
t58 = t5
t61 = is_int(t56)
if t61:
    t62 = is_int(t58)
    if t62:
        t63 = project_int(t56)
        t64 = project_int(t58)
        t65 = t63 == t64
        t6 = inject_bool(t65)
    else:
        t66 = is_bool(t58)
        if t66:
            t67 = project_int(t56)
            t68 = project_bool(t58)
            t69 = t67 == t68
            t6 = inject_bool(t69)
        else:
            t70 = project_int(t56)
            t71 = project_big(t58)
            t72 = t70 == t71
            t6 = inject_bool(t72)
else:
    t73 = is_bool(t56)
    if t73:
        t74 = is_int(t58)
        if t74:
            t75 = project_bool(t56)
            t76 = project_int(t58)
            t77 = t75 == t76
            t6 = inject_bool(t77)
        else:
            t78 = is_bool(t58)
            if t78:
                t79 = project_bool(t56)
                t80 = project_bool(t58)
                t81 = t79 == t80
                t6 = inject_bool(t81)
            else:
                t82 = project_bool(t56)
                t83 = project_big(t58)
                t84 = t82 == t83
                t6 = inject_bool(t84)
    else:
        t85 = is_int(t58)
        if t85:
            t86 = project_big(t56)
            t87 = project_int(t58)
            t88 = t86 == t87
            t6 = inject_bool(t88)
        else:
            t89 = is_bool(t58)
            if t89:
                t90 = project_big(t56)
                t91 = project_bool(t58)
                t92 = t90 == t91
                t6 = inject_bool(t92)
            else:
                t93 = project_big(t56)
                t94 = project_big(t58)
                t95 = equal(t93, t94)
                t6 = inject_bool(t95)