Module(
    body=[
        Assign(
            targets=[
                Name(id='t118', ctx=Store())],
            value=Name(id='t9', ctx=Load())),
        Assign(
            targets=[
                Name(id='t121', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t118', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t121', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t122', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t118', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t123', ctx=Store())],
                    value=UnaryOp(
                        op=USub(),
                        operand=Name(id='t122', ctx=Load()))),
                Assign(
                    targets=[
                        Name(id='t10', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
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
                            Name(id='t118', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t124', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t125', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t118', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t126', ctx=Store())],
                            value=UnaryOp(
                                op=USub(),
                                operand=Name(id='t125', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t10', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t126', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])])],
    type_ignores=[])