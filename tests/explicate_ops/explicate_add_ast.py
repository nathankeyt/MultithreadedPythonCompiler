Module(
    body=[
        Assign(
            targets=[
                Name(id='t16', ctx=Store())],
            value=Name(id='t2', ctx=Load())),
        Assign(
            targets=[
                Name(id='t18', ctx=Store())],
            value=Name(id='t3', ctx=Load())),
        Assign(
            targets=[
                Name(id='t21', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t16', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t21', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t22', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t18', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t22', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t23', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t16', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t24', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t18', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t25', ctx=Store())],
                            value=BinOp(
                                left=Name(id='t23', ctx=Load()),
                                op=Add(),
                                right=Name(id='t24', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t4', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t25', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t26', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t18', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t26', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t27', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t16', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t28', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t18', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t29', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t27', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t28', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t4', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t29', ctx=Load())],
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
                        Name(id='t30', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t16', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t30', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t31', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t18', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t31', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t32', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t16', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t33', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t18', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t34', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t32', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t33', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t4', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t34', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t35', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t18', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t35', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t36', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t16', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t37', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t18', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t38', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='t36', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='t37', ctx=Load()))),
                                        Assign(
                                            targets=[
                                                Name(id='t4', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_int', ctx=Load()),
                                                args=[
                                                    Name(id='t38', ctx=Load())],
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
                                Name(id='t39', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t18', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t39', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[]),
                        Assign(
                            targets=[
                                Name(id='t40', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t18', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t40', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t41', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_big', ctx=Load()),
                                        args=[
                                            Name(id='t18', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t41', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t42', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t16', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t43', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t18', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t44', ctx=Store())],
                                            value=Call(
                                                func=Name(id='add', ctx=Load()),
                                                args=[
                                                    Name(id='t42', ctx=Load()),
                                                    Name(id='t43', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t4', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_big', ctx=Load()),
                                                args=[
                                                    Name(id='t44', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[])])])])],
    type_ignores=[])