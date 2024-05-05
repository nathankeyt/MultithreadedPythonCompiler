Module(
    body=[
        Assign(
            targets=[
                Name(id='t68', ctx=Store())],
            value=Name(id='t6', ctx=Load())),
        Assign(
            targets=[
                Name(id='t70', ctx=Store())],
            value=Name(id='t7', ctx=Load())),
        Assign(
            targets=[
                Name(id='t73', ctx=Store())],
            value=Call(
                func=Name(id='is_true', ctx=Load()),
                args=[
                    Name(id='t68', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t73', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t2', ctx=Store())],
                    value=Name(id='t68', ctx=Load()))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t2', ctx=Store())],
                    value=Name(id='t70', ctx=Load()))])],
    type_ignores=[])