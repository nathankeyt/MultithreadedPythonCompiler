Module(
    body=[
        Assign(
            targets=[
                Name(id='t149', ctx=Store())],
            value=Name(id='t2', ctx=Load())),
        Assign(
            targets=[
                Name(id='t152', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t149', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t152', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t153', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t149', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t3', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t153', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t154', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t149', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t154', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t155', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t149', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t3', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t155', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t156', ctx=Store())],
                            value=Call(
                                func=Name(id='is_big', ctx=Load()),
                                args=[
                                    Name(id='t149', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t156', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[])])])],
    type_ignores=[])