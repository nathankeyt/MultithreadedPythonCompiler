Module(
    body=[
        Assign(
            targets=[
                Name(id='t90', ctx=Store())],
            value=Name(id='t12', ctx=Load())),
        Assign(
            targets=[
                Name(id='t93', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t90', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t93', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t94', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t90', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t95', ctx=Store())],
                    value=UnaryOp(
                        op=USub(),
                        operand=Name(id='t94', ctx=Load()))),
                Assign(
                    targets=[
                        Name(id='t13', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t95', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t96', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t90', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t96', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t97', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t90', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t98', ctx=Store())],
                            value=UnaryOp(
                                op=USub(),
                                operand=Name(id='t97', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t13', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t98', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])])],
    type_ignores=[])