Module(
    body=[
        Assign(
            targets=[
                Name(id='x', ctx=Store())],
            value=Constant(value=2)),
        Assign(
            targets=[
                Name(id='y', ctx=Store())],
            value=Constant(value=3)),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Name(id='x', ctx=Load())],
                keywords=[])),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Name(id='y', ctx=Load())],
                keywords=[])),
        Assign(
            targets=[
                Name(id='tmp', ctx=Store())],
            value=Name(id='x', ctx=Load())),
        Assign(
            targets=[
                Name(id='x', ctx=Store())],
            value=Name(id='y', ctx=Load())),
        Assign(
            targets=[
                Name(id='y', ctx=Store())],
            value=Name(id='tmp', ctx=Load())),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Name(id='x', ctx=Load())],
                keywords=[])),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Name(id='y', ctx=Load())],
                keywords=[]))],
    type_ignores=[])