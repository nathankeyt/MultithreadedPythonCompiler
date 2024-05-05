Module(
    body=[
        Assign(
            targets=[
                Name(id='t0', ctx=Store())],
            value=Call(
                func=Name(id='inject_int', ctx=Load()),
                args=[
                    Constant(value=2)],
                keywords=[])),
        Assign(
            targets=[
                Name(id='t1', ctx=Store())],
            value=Call(
                func=Name(id='inject_int', ctx=Load()),
                args=[
                    Constant(value=3)],
                keywords=[])),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Name(id='t0', ctx=Load())],
                keywords=[])),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Name(id='t1', ctx=Load())],
                keywords=[])),
        Assign(
            targets=[
                Name(id='t2', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t0', ctx=Store())],
            value=Name(id='t1', ctx=Load())),
        Assign(
            targets=[
                Name(id='t1', ctx=Store())],
            value=Name(id='t2', ctx=Load())),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Name(id='t0', ctx=Load())],
                keywords=[])),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Name(id='t1', ctx=Load())],
                keywords=[]))],
    type_ignores=[])