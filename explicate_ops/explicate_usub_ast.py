Module(
    body=[
        Assign(
            targets=[
                Name(id='t1035', ctx=Store())],
            value=Name(id='t32', ctx=Load())),
        Assign(
            targets=[
                Name(id='t1038', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t1035', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t1038', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t1039', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t1035', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t1040', ctx=Store())],
                    value=UnaryOp(
                        op=USub(),
                        operand=Name(id='t1039', ctx=Load()))),
                Assign(
                    targets=[
                        Name(id='t33', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t1040', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t1041', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t1035', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t1041', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t1042', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t1035', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t1043', ctx=Store())],
                            value=UnaryOp(
                                op=USub(),
                                operand=Name(id='t1042', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t33', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t1043', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])])],
    type_ignores=[])