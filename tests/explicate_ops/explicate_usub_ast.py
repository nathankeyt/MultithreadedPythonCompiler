Module(
    body=[
        Assign(
            targets=[
                Name(id='t2', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t5', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t2', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t5', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t6', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t2', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t7', ctx=Store())],
                    value=UnaryOp(
                        op=USub(),
                        operand=Name(id='t6', ctx=Load()))),
                Assign(
                    targets=[
                        Name(id='t1', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t7', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t8', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t2', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t8', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t9', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t2', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t10', ctx=Store())],
                            value=UnaryOp(
                                op=USub(),
                                operand=Name(id='t9', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t1', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t10', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])])],
    type_ignores=[])