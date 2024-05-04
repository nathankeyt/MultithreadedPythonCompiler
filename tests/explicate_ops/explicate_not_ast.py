Module(
    body=[
        Assign(
            targets=[
                Name(id='t691', ctx=Store())],
            value=Name(id='t4', ctx=Load())),
        Assign(
            targets=[
                Name(id='t694', ctx=Store())],
            value=Call(
                func=Name(id='is_true', ctx=Load()),
                args=[
                    Name(id='t691', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t694', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t42', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_bool', ctx=Load()),
                        args=[
                            Constant(value=0)],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t42', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_bool', ctx=Load()),
                        args=[
                            Constant(value=1)],
                        keywords=[]))])],
    type_ignores=[])