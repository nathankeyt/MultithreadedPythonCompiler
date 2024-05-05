Module(
    body=[
        Assign(
            targets=[
                Name(id='t0', ctx=Store())],
            value=Call(
                func=Name(id='inject_int', ctx=Load()),
                args=[
                    Constant(value=1)],
                keywords=[])),
        Assign(
            targets=[
                Name(id='t1', ctx=Store())],
            value=UnaryOp(
                op=USub(),
                operand=Name(id='t0', ctx=Load()))),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Name(id='t1', ctx=Load())],
                keywords=[]))],
    type_ignores=[])