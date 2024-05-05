Module(
    body=[
        Assign(
            targets=[
                Name(id='t4', ctx=Store())],
            value=Name(id='t2', ctx=Load())),
        Assign(
            targets=[
                Name(id='t7', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t4', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t7', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t8', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t4', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t9', ctx=Store())],
                    value=UnaryOp(
                        op=USub(),
                        operand=Name(id='t8', ctx=Load()))),
                Assign(
                    targets=[
                        Name(id='t1', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t9', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t10', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t4', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t10', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t11', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t4', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t12', ctx=Store())],
                            value=UnaryOp(
                                op=USub(),
                                operand=Name(id='t11', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t1', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t12', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])])],
    type_ignores=[])