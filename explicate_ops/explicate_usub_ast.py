Module(
    body=[
        Assign(
            targets=[
                Name(id='t435', ctx=Store())],
            value=Name(id='t13', ctx=Load())),
        Assign(
            targets=[
                Name(id='t438', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t435', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t438', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t439', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t435', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t440', ctx=Store())],
                    value=UnaryOp(
                        op=USub(),
                        operand=Name(id='t439', ctx=Load()))),
                Assign(
                    targets=[
                        Name(id='t14', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t440', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t441', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t435', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t441', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t442', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t435', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t443', ctx=Store())],
                            value=UnaryOp(
                                op=USub(),
                                operand=Name(id='t442', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t14', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t443', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])])],
    type_ignores=[])