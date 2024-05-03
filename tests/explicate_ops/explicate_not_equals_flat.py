t83 = t0
t85 = t1
t88 = is_int(t83)
if t88:
    t89 = is_int(t85)
    if t89:
        t90 = project_int(t83)
        t91 = project_int(t85)
        t92 = t90 != t91
        t2 = inject_bool(t92)
    else:
        t93 = is_bool(t85)
        if t93:
            t94 = project_int(t83)
            t95 = project_bool(t85)
            t96 = t94 != t95
            t2 = inject_bool(t96)
        else:
            t97 = project_int(t83)
            t98 = project_big(t85)
            t99 = t97 != t98
            t2 = inject_bool(t99)
else:
    t100 = is_bool(t83)
    if t100:
        t101 = is_int(t85)
        if t101:
            t102 = project_bool(t83)
            t103 = project_int(t85)
            t104 = t102 != t103
            t2 = inject_bool(t104)
        else:
            t105 = is_bool(t85)
            if t105:
                t106 = project_bool(t83)
                t107 = project_bool(t85)
                t108 = t106 != t107
                t2 = inject_bool(t108)
            else:
                t109 = project_bool(t83)
                t110 = project_big(t85)
                t111 = t109 != t110
                t2 = inject_bool(t111)
    else:
        t112 = is_int(t85)
        if t112:
            t113 = project_big(t83)
            t114 = project_int(t85)
            t115 = t113 != t114
            t2 = inject_bool(t115)
        else:
            t116 = is_bool(t85)
            if t116:
                t117 = project_big(t83)
                t118 = project_bool(t85)
                t119 = t117 != t118
                t2 = inject_bool(t119)
            else:
                t120 = project_big(t83)
                t121 = project_big(t85)
                t122 = not_equal(t120, t121)
                t2 = inject_bool(t122)