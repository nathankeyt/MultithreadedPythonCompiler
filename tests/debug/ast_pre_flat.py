Module(
    body=[
        Assign(
            targets=[
                Name(id='t0', ctx=Store())],
            value=Constant(value=1)),
        Assign(
            targets=[
                Name(id='t1', ctx=Store())],
            value=Constant(value=100)),
        While(
            test=Call(
                func=Name(id='int', ctx=Load()),
                args=[
                    Compare(
                        left=Name(id='t0', ctx=Load()),
                        ops=[
                            NotEq()],
                        comparators=[
                            Name(id='t1', ctx=Load())])],
                keywords=[]),
            body=[
                Assign(
                    targets=[
                        Name(id='t0', ctx=Store())],
                    value=BinOp(
                        left=Name(id='t0', ctx=Load()),
                        op=Add(),
                        right=Constant(value=1))),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            BoolOp(
                                op=And(),
                                values=[
                                    Name(id='t0', ctx=Load()),
                                    Name(id='t1', ctx=Load())])],
                        keywords=[]))],
            orelse=[])],
    type_ignores=[])