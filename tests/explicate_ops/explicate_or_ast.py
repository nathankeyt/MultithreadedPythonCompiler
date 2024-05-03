Module(
    body=[
        Assign(
            targets=[
                Name(id='t3', ctx=Store())],
            value=Name(id='t1', ctx=Load())),
        Assign(
            targets=[
                Name(id='t5', ctx=Store())],
            value=Name(id='t2', ctx=Load())),
        Assign(
            targets=[
                Name(id='t8', ctx=Store())],
            value=Call(
                func=Name(id='is_true', ctx=Load()),
                args=[
                    Name(id='t3', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t8', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t0', ctx=Store())],
                    value=Name(id='t3', ctx=Load()))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t0', ctx=Store())],
                    value=Name(id='t5', ctx=Load()))])],
    type_ignores=[])