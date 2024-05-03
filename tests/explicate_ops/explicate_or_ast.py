Module(
    body=[
        Assign(
            targets=[
                Name(id='t482', ctx=Store())],
            value=Name(id='t29', ctx=Load())),
        Assign(
            targets=[
                Name(id='t484', ctx=Store())],
            value=Name(id='t32', ctx=Load())),
        Assign(
            targets=[
                Name(id='t487', ctx=Store())],
            value=Call(
                func=Name(id='is_true', ctx=Load()),
                args=[
                    Name(id='t482', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t487', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t33', ctx=Store())],
                    value=Name(id='t482', ctx=Load()))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t33', ctx=Store())],
                    value=Name(id='t484', ctx=Load()))])],
    type_ignores=[])