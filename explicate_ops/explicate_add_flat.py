t72 = t26
t74 = t7
t77 = is_int(t72)
if t77:
    t78 = is_int(t74)
    if t78:
        t79 = project_int(t72)
        t80 = project_int(t74)
        t81 = t79 + t80
        t27 = inject_int(t81)
    else:
        t82 = is_bool(t74)
        if t82:
            t83 = project_int(t72)
            t84 = project_bool(t74)
            t85 = t83 + t84
            t27 = inject_int(t85)
        else:
            throw_type_error()
else:
    t86 = is_bool(t72)
    if t86:
        t87 = is_int(t74)
        if t87:
            t88 = project_bool(t72)
            t89 = project_int(t74)
            t90 = t88 + t89
            t27 = inject_int(t90)
        else:
            t91 = is_bool(t74)
            if t91:
                t92 = project_bool(t72)
                t93 = project_bool(t74)
                t94 = t92 + t93
                t27 = inject_int(t94)
            else:
                throw_type_error()
    else:
        t95 = is_int(t74)
        if t95:
            throw_type_error()
        t96 = is_int(t74)
        if t96:
            throw_type_error()
        else:
            t97 = is_big(t74)
            if t97:
                t98 = project_big(t72)
                t99 = project_big(t74)
                t100 = add(t98, t99)
                t27 = inject_big(t100)