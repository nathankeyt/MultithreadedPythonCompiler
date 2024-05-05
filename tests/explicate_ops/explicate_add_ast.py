Module(
    body=[
        Assign(
            targets=[
                Name(id='t3', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t5', ctx=Store())],
            value=Name(id='t1', ctx=Load())),
        Assign(
            targets=[
                Name(id='t8', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t3', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t8', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t9', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t5', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t9', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t10', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t3', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t11', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t5', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t12', ctx=Store())],
                            value=BinOp(
                                left=Name(id='t10', ctx=Load()),
                                op=Add(),
                                right=Name(id='t11', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t2', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t12', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t13', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t5', ctx=Load())],
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
                                            Name(id='t3', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t15', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t5', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t16', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t14', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t15', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t16', ctx=Load())],
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
                        Name(id='t17', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t3', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t17', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t18', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t5', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t18', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t19', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t3', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t20', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t5', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t21', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t19', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t20', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t21', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t22', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t5', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t22', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t23', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t3', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t24', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t5', ctx=Load())],
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
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_int', ctx=Load()),
                                                args=[
                                                    Name(id='t25', ctx=Load())],
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
                                Name(id='t26', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t5', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t26', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[]),
                        Assign(
                            targets=[
                                Name(id='t27', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t5', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t27', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t28', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_big', ctx=Load()),
                                        args=[
                                            Name(id='t5', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t28', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t29', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t3', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t30', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t5', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t31', ctx=Store())],
                                            value=Call(
                                                func=Name(id='add', ctx=Load()),
                                                args=[
                                                    Name(id='t29', ctx=Load()),
                                                    Name(id='t30', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_big', ctx=Load()),
                                                args=[
                                                    Name(id='t31', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[])])])])],
    type_ignores=[])