Module(
    body=[
        Assign(
            targets=[
                Name(id='t558', ctx=Store())],
            value=Name(id='t39', ctx=Load())),
        Assign(
            targets=[
                Name(id='t561', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t558', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t561', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t562', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t558', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t563', ctx=Store())],
                    value=UnaryOp(
                        op=USub(),
                        operand=Name(id='t562', ctx=Load()))),
                Assign(
                    targets=[
                        Name(id='t40', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t563', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t564', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t558', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t564', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t565', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t558', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t566', ctx=Store())],
                            value=UnaryOp(
                                op=USub(),
                                operand=Name(id='t565', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t40', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t566', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])])],
    type_ignores=[])