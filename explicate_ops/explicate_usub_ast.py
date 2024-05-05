Module(
    body=[
        Assign(
            targets=[
                Name(id='t172', ctx=Store())],
            value=Name(id='t16', ctx=Load())),
        Assign(
            targets=[
                Name(id='t175', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t172', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t175', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t176', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t172', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t177', ctx=Store())],
                    value=UnaryOp(
                        op=USub(),
                        operand=Name(id='t176', ctx=Load()))),
                Assign(
                    targets=[
                        Name(id='t17', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t177', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t178', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t172', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t178', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t179', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t172', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t180', ctx=Store())],
                            value=UnaryOp(
                                op=USub(),
                                operand=Name(id='t179', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t17', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t180', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])])],
    type_ignores=[])