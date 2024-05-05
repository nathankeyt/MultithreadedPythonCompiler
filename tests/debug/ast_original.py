Module(
    body=[
        Assign(
            targets=[
                Name(id='x', ctx=Store())],
            value=Constant(value=1)),
        Assign(
            targets=[
                Name(id='y', ctx=Store())],
            value=Constant(value=100)),
        While(
            test=Call(
                func=Name(id='int', ctx=Load()),
                args=[
                    Compare(
                        left=Name(id='x', ctx=Load()),
                        ops=[
                            NotEq()],
                        comparators=[
                            Name(id='y', ctx=Load())])],
                keywords=[]),
            body=[
                Assign(
                    targets=[
                        Name(id='x', ctx=Store())],
                    value=BinOp(
                        left=Name(id='x', ctx=Load()),
                        op=Add(),
                        right=Constant(value=1))),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            BoolOp(
                                op=And(),
                                values=[
                                    Name(id='x', ctx=Load()),
                                    Name(id='y', ctx=Load())])],
                        keywords=[]))],
            orelse=[])],
    type_ignores=[])