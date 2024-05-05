t0 = inject_int(1)
t1 = inject_int(100)
t7 = t0
t9 = t1
t12 = is_int(t7)
if t12:
    t13 = is_int(t9)
    if t13:
        t14 = project_int(t7)
        t15 = project_int(t9)
        t16 = t14 != t15
        t2 = inject_bool(t16)
    else:
        t17 = is_bool(t9)
        if t17:
            t18 = project_int(t7)
            t19 = project_bool(t9)
            t20 = t18 != t19
            t2 = inject_bool(t20)
        else:
            t21 = project_int(t7)
            t22 = project_big(t9)
            t23 = t21 != t22
            t2 = inject_bool(t23)
else:
    t24 = is_bool(t7)
    if t24:
        t25 = is_int(t9)
        if t25:
            t26 = project_bool(t7)
            t27 = project_int(t9)
            t28 = t26 != t27
            t2 = inject_bool(t28)
        else:
            t29 = is_bool(t9)
            if t29:
                t30 = project_bool(t7)
                t31 = project_bool(t9)
                t32 = t30 != t31
                t2 = inject_bool(t32)
            else:
                t33 = project_bool(t7)
                t34 = project_big(t9)
                t35 = t33 != t34
                t2 = inject_bool(t35)
    else:
        t36 = is_int(t9)
        if t36:
            t37 = project_big(t7)
            t38 = project_int(t9)
            t39 = t37 != t38
            t2 = inject_bool(t39)
        else:
            t40 = is_bool(t9)
            if t40:
                t41 = project_big(t7)
                t42 = project_bool(t9)
                t43 = t41 != t42
                t2 = inject_bool(t43)
            else:
                t44 = project_big(t7)
                t45 = project_big(t9)
                t46 = not_equal(t44, t45)
                t2 = inject_bool(t46)
t47 = t2
t50 = is_int(t47)
if t50:
    t51 = project_int(t47)
    t3 = inject_int(t51)
else:
    t52 = is_bool(t47)
    if t52:
        t53 = project_bool(t47)
        t3 = inject_int(t53)
    else:
        throw_type_error()
t4 = is_true(t3)
while t4:
    t5 = inject_int(1)
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
    t83 = t0
    t85 = t1
    t88 = is_true(t85)
    if t88:
        t89 = is_true(t83)
        if t89:
            t6 = t85
        else:
            t6 = t83
    else:
        t90 = is_true(t83)
        if t90:
            t6 = t85
        else:
            t6 = t83
    print(t6)
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
    t131 = t2
    t134 = is_int(t131)
    if t134:
        t135 = project_int(t131)
        t3 = inject_int(t135)
    else:
        t136 = is_bool(t131)
        if t136:
            t137 = project_bool(t131)
            t3 = inject_int(t137)
        else:
            throw_type_error()
    t4 = is_true(t3)