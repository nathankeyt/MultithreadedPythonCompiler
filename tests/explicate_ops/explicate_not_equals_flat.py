t91 = t0
t93 = t1
t96 = is_int(t91)
if t96:
    t97 = is_int(t93)
    if t97:
        t98 = project_int(t91)
        t99 = project_int(t93)
        t100 = t98 != t99
        t2 = inject_bool(t100)
    else:
        t101 = is_bool(t93)
        if t101:
            t102 = project_int(t91)
            t103 = project_bool(t93)
            t104 = t102 != t103
            t2 = inject_bool(t104)
        else:
            t105 = project_int(t91)
            t106 = project_big(t93)
            t107 = t105 != t106
            t2 = inject_bool(t107)
else:
    t108 = is_bool(t91)
    if t108:
        t109 = is_int(t93)
        if t109:
            t110 = project_bool(t91)
            t111 = project_int(t93)
            t112 = t110 != t111
            t2 = inject_bool(t112)
        else:
            t113 = is_bool(t93)
            if t113:
                t114 = project_bool(t91)
                t115 = project_bool(t93)
                t116 = t114 != t115
                t2 = inject_bool(t116)
            else:
                t117 = project_bool(t91)
                t118 = project_big(t93)
                t119 = t117 != t118
                t2 = inject_bool(t119)
    else:
        t120 = is_int(t93)
        if t120:
            t121 = project_big(t91)
            t122 = project_int(t93)
            t123 = t121 != t122
            t2 = inject_bool(t123)
        else:
            t124 = is_bool(t93)
            if t124:
                t125 = project_big(t91)
                t126 = project_bool(t93)
                t127 = t125 != t126
                t2 = inject_bool(t127)
            else:
                t128 = project_big(t91)
                t129 = project_big(t93)
                t130 = not_equal(t128, t129)
                t2 = inject_bool(t130)