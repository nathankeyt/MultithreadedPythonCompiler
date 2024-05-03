Module(
    body=[
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
                    Name(id='t9', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t12', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t13', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t9', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t2', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t13', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t14', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t9', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t14', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t15', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t9', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t2', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t15', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])])],
    type_ignores=[])