Module(
    body=[
        Assign(
            targets=[
                Name(id='t6', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t9', ctx=Store())],
            value=Call(
                func=Name(id='is_true', ctx=Load()),
                args=[
                    Name(id='t6', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t9', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t1', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_bool', ctx=Load()),
                        args=[
                            Constant(value=0)],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t1', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_bool', ctx=Load()),
                        args=[
                            Constant(value=1)],
                        keywords=[]))])],
    type_ignores=[])