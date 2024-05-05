Module(
    body=[
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    UnaryOp(
                        op=USub(),
                        operand=Constant(value=1))],
                keywords=[]))],
    type_ignores=[])