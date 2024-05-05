Module(
    body=[
        Assign(
            targets=[
                Name(id='t0', ctx=Store())],
            value=Call(
                func=Name(id='inject_int', ctx=Load()),
                args=[
                    Constant(value=1)],
                keywords=[])),
        Assign(
            targets=[
                Name(id='t1', ctx=Store())],
            value=Call(
                func=Name(id='inject_int', ctx=Load()),
                args=[
                    Constant(value=100)],
                keywords=[])),
        Assign(
            targets=[
                Name(id='t7', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t9', ctx=Store())],
            value=Name(id='t1', ctx=Load())),
        Assign(
            targets=[
                Name(id='t12', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t7', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t12', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t13', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t9', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t13', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t14', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t7', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t15', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t9', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t16', ctx=Store())],
                            value=Compare(
                                left=Name(id='t14', ctx=Load()),
                                ops=[
                                    NotEq()],
                                comparators=[
                                    Name(id='t15', ctx=Load())])),
                        Assign(
                            targets=[
                                Name(id='t2', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_bool', ctx=Load()),
                                args=[
                                    Name(id='t16', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t17', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t9', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t17', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t18', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t7', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t19', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t9', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t20', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t18', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t19', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t20', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t21', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t7', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t22', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t9', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t23', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t21', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t22', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t23', ctx=Load())],
                                        keywords=[]))])])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t24', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t7', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t24', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t25', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t9', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t25', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t26', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t7', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t27', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t9', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t28', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t26', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t27', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t28', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t29', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t9', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t29', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t30', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t7', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t31', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t9', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t32', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t30', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t31', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t32', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t33', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t7', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t34', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t9', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t35', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t33', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t34', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t35', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t36', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t9', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t36', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t37', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t7', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t38', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t9', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t39', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t37', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t38', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t39', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t40', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t9', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t40', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t41', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t7', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t42', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t9', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t43', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t41', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t42', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t43', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t44', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t7', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t45', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t9', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t46', ctx=Store())],
                                            value=Call(
                                                func=Name(id='not_equal', ctx=Load()),
                                                args=[
                                                    Name(id='t44', ctx=Load()),
                                                    Name(id='t45', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t46', ctx=Load())],
                                                keywords=[]))])])])]),
        Assign(
            targets=[
                Name(id='t47', ctx=Store())],
            value=Name(id='t2', ctx=Load())),
        Assign(
            targets=[
                Name(id='t50', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t47', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t50', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t51', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t47', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t3', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t51', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t52', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t47', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t52', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t53', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t47', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t3', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t53', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])]),
        Assign(
            targets=[
                Name(id='t4', ctx=Store())],
            value=Call(
                func=Name(id='is_true', ctx=Load()),
                args=[
                    Name(id='t3', ctx=Load())],
                keywords=[])),
        While(
            test=Name(id='t4', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t5', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Constant(value=1)],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t54', ctx=Store())],
                    value=Name(id='t0', ctx=Load())),
                Assign(
                    targets=[
                        Name(id='t56', ctx=Store())],
                    value=Name(id='t5', ctx=Load())),
                Assign(
                    targets=[
                        Name(id='t59', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t54', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t59', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t60', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t56', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t60', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t61', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t54', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t62', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t56', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t63', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t61', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t62', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t0', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t63', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t64', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t56', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t64', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t65', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_int', ctx=Load()),
                                                args=[
                                                    Name(id='t54', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t66', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t56', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t67', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='t65', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='t66', ctx=Load()))),
                                        Assign(
                                            targets=[
                                                Name(id='t0', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_int', ctx=Load()),
                                                args=[
                                                    Name(id='t67', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='throw_type_error', ctx=Load()),
                                                args=[],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t68', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t54', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t68', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t69', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_int', ctx=Load()),
                                        args=[
                                            Name(id='t56', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t69', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t70', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t54', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t71', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_int', ctx=Load()),
                                                args=[
                                                    Name(id='t56', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t72', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='t70', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='t71', ctx=Load()))),
                                        Assign(
                                            targets=[
                                                Name(id='t0', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_int', ctx=Load()),
                                                args=[
                                                    Name(id='t72', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t73', ctx=Store())],
                                            value=Call(
                                                func=Name(id='is_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t56', ctx=Load())],
                                                keywords=[])),
                                        If(
                                            test=Name(id='t73', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Name(id='t74', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='project_bool', ctx=Load()),
                                                        args=[
                                                            Name(id='t54', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t75', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='project_bool', ctx=Load()),
                                                        args=[
                                                            Name(id='t56', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t76', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='t74', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='t75', ctx=Load()))),
                                                Assign(
                                                    targets=[
                                                        Name(id='t0', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='inject_int', ctx=Load()),
                                                        args=[
                                                            Name(id='t76', ctx=Load())],
                                                        keywords=[]))],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='throw_type_error', ctx=Load()),
                                                        args=[],
                                                        keywords=[]))])])],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t77', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_int', ctx=Load()),
                                        args=[
                                            Name(id='t56', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t77', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='throw_type_error', ctx=Load()),
                                                args=[],
                                                keywords=[]))],
                                    orelse=[]),
                                Assign(
                                    targets=[
                                        Name(id='t78', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_int', ctx=Load()),
                                        args=[
                                            Name(id='t56', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t78', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='throw_type_error', ctx=Load()),
                                                args=[],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t79', ctx=Store())],
                                            value=Call(
                                                func=Name(id='is_big', ctx=Load()),
                                                args=[
                                                    Name(id='t56', ctx=Load())],
                                                keywords=[])),
                                        If(
                                            test=Name(id='t79', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Name(id='t80', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='project_big', ctx=Load()),
                                                        args=[
                                                            Name(id='t54', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t81', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='project_big', ctx=Load()),
                                                        args=[
                                                            Name(id='t56', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t82', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='add', ctx=Load()),
                                                        args=[
                                                            Name(id='t80', ctx=Load()),
                                                            Name(id='t81', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t0', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='inject_big', ctx=Load()),
                                                        args=[
                                                            Name(id='t82', ctx=Load())],
                                                        keywords=[]))],
                                            orelse=[])])])]),
                Assign(
                    targets=[
                        Name(id='t83', ctx=Store())],
                    value=Name(id='t0', ctx=Load())),
                Assign(
                    targets=[
                        Name(id='t85', ctx=Store())],
                    value=Name(id='t1', ctx=Load())),
                Assign(
                    targets=[
                        Name(id='t88', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t85', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t88', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t89', ctx=Store())],
                            value=Call(
                                func=Name(id='is_true', ctx=Load()),
                                args=[
                                    Name(id='t83', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t89', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Name(id='t85', ctx=Load()))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Name(id='t83', ctx=Load()))])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t90', ctx=Store())],
                            value=Call(
                                func=Name(id='is_true', ctx=Load()),
                                args=[
                                    Name(id='t83', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t90', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Name(id='t85', ctx=Load()))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Name(id='t83', ctx=Load()))])]),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            Name(id='t6', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t91', ctx=Store())],
                    value=Name(id='t0', ctx=Load())),
                Assign(
                    targets=[
                        Name(id='t93', ctx=Store())],
                    value=Name(id='t1', ctx=Load())),
                Assign(
                    targets=[
                        Name(id='t96', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t91', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t96', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t97', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t93', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t97', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t98', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t91', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t99', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t93', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t100', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t98', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t99', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t100', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t101', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t93', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t101', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t102', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_int', ctx=Load()),
                                                args=[
                                                    Name(id='t91', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t103', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t93', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t104', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t102', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t103', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t104', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t105', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_int', ctx=Load()),
                                                args=[
                                                    Name(id='t91', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t106', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t93', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t107', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t105', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t106', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t107', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t108', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t91', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t108', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t109', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_int', ctx=Load()),
                                        args=[
                                            Name(id='t93', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t109', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t110', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t91', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t111', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_int', ctx=Load()),
                                                args=[
                                                    Name(id='t93', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t112', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t110', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t111', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t112', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t113', ctx=Store())],
                                            value=Call(
                                                func=Name(id='is_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t93', ctx=Load())],
                                                keywords=[])),
                                        If(
                                            test=Name(id='t113', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Name(id='t114', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='project_bool', ctx=Load()),
                                                        args=[
                                                            Name(id='t91', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t115', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='project_bool', ctx=Load()),
                                                        args=[
                                                            Name(id='t93', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t116', ctx=Store())],
                                                    value=Compare(
                                                        left=Name(id='t114', ctx=Load()),
                                                        ops=[
                                                            NotEq()],
                                                        comparators=[
                                                            Name(id='t115', ctx=Load())])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t2', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='inject_bool', ctx=Load()),
                                                        args=[
                                                            Name(id='t116', ctx=Load())],
                                                        keywords=[]))],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Name(id='t117', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='project_bool', ctx=Load()),
                                                        args=[
                                                            Name(id='t91', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t118', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='project_big', ctx=Load()),
                                                        args=[
                                                            Name(id='t93', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t119', ctx=Store())],
                                                    value=Compare(
                                                        left=Name(id='t117', ctx=Load()),
                                                        ops=[
                                                            NotEq()],
                                                        comparators=[
                                                            Name(id='t118', ctx=Load())])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t2', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='inject_bool', ctx=Load()),
                                                        args=[
                                                            Name(id='t119', ctx=Load())],
                                                        keywords=[]))])])],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t120', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_int', ctx=Load()),
                                        args=[
                                            Name(id='t93', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t120', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t121', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t91', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t122', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_int', ctx=Load()),
                                                args=[
                                                    Name(id='t93', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t123', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t121', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t122', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t123', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t124', ctx=Store())],
                                            value=Call(
                                                func=Name(id='is_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t93', ctx=Load())],
                                                keywords=[])),
                                        If(
                                            test=Name(id='t124', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Name(id='t125', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='project_big', ctx=Load()),
                                                        args=[
                                                            Name(id='t91', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t126', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='project_bool', ctx=Load()),
                                                        args=[
                                                            Name(id='t93', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t127', ctx=Store())],
                                                    value=Compare(
                                                        left=Name(id='t125', ctx=Load()),
                                                        ops=[
                                                            NotEq()],
                                                        comparators=[
                                                            Name(id='t126', ctx=Load())])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t2', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='inject_bool', ctx=Load()),
                                                        args=[
                                                            Name(id='t127', ctx=Load())],
                                                        keywords=[]))],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Name(id='t128', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='project_big', ctx=Load()),
                                                        args=[
                                                            Name(id='t91', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t129', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='project_big', ctx=Load()),
                                                        args=[
                                                            Name(id='t93', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t130', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='not_equal', ctx=Load()),
                                                        args=[
                                                            Name(id='t128', ctx=Load()),
                                                            Name(id='t129', ctx=Load())],
                                                        keywords=[])),
                                                Assign(
                                                    targets=[
                                                        Name(id='t2', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='inject_bool', ctx=Load()),
                                                        args=[
                                                            Name(id='t130', ctx=Load())],
                                                        keywords=[]))])])])]),
                Assign(
                    targets=[
                        Name(id='t131', ctx=Store())],
                    value=Name(id='t2', ctx=Load())),
                Assign(
                    targets=[
                        Name(id='t134', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t131', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t134', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t135', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t131', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t3', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t135', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t136', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t131', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t136', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t137', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t131', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t3', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t137', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))])]),
                Assign(
                    targets=[
                        Name(id='t4', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t3', ctx=Load())],
                        keywords=[]))],
            orelse=[])],
    type_ignores=[])