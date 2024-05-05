Module(
    body=[
        Assign(
            targets=[
                Name(id='t131', ctx=Store())],
            value=Name(id='t2', ctx=Load())),
        Assign(
            targets=[
                Name(id='t134', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t131', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t134', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t135', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t131', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t3', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t135', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t136', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t131', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t136', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t137', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t131', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t3', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t137', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])])],
    type_ignores=[])