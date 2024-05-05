t94 = t6
t96 = t11
t99 = is_int(t94)
if t99:
    t100 = is_int(t96)
    if t100:
        t101 = project_int(t94)
        t102 = project_int(t96)
        t103 = t101 == t102
        t12 = inject_bool(t103)
    else:
        t104 = is_bool(t96)
        if t104:
            t105 = project_int(t94)
            t106 = project_bool(t96)
            t107 = t105 == t106
            t12 = inject_bool(t107)
        else:
            t108 = project_int(t94)
            t109 = project_big(t96)
            t110 = t108 == t109
            t12 = inject_bool(t110)
else:
    t111 = is_bool(t94)
    if t111:
        t112 = is_int(t96)
        if t112:
            t113 = project_bool(t94)
            t114 = project_int(t96)
            t115 = t113 == t114
            t12 = inject_bool(t115)
        else:
            t116 = is_bool(t96)
            if t116:
                t117 = project_bool(t94)
                t118 = project_bool(t96)
                t119 = t117 == t118
                t12 = inject_bool(t119)
            else:
                t120 = project_bool(t94)
                t121 = project_big(t96)
                t122 = t120 == t121
                t12 = inject_bool(t122)
    else:
        t123 = is_int(t96)
        if t123:
            t124 = project_big(t94)
            t125 = project_int(t96)
            t126 = t124 == t125
            t12 = inject_bool(t126)
        else:
            t127 = is_bool(t96)
            if t127:
                t128 = project_big(t94)
                t129 = project_bool(t96)
                t130 = t128 == t129
                t12 = inject_bool(t130)
            else:
                t131 = project_big(t94)
                t132 = project_big(t96)
                t133 = equal(t131, t132)
                t12 = inject_bool(t133)