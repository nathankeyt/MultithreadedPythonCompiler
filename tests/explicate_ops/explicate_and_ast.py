Module(
    body=[
        Assign(
            targets=[
                Name(id='t83', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t85', ctx=Store())],
            value=Name(id='t1', ctx=Load())),
        Assign(
            targets=[
                Name(id='t88', ctx=Store())],
            value=Call(
                func=Name(id='is_true', ctx=Load()),
                args=[
                    Name(id='t85', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t88', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t89', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t83', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t89', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t6', ctx=Store())],
                            value=Name(id='t85', ctx=Load()))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t6', ctx=Store())],
                            value=Name(id='t83', ctx=Load()))])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t90', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t83', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t90', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t6', ctx=Store())],
                            value=Name(id='t85', ctx=Load()))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t6', ctx=Store())],
                            value=Name(id='t83', ctx=Load()))])])],
    type_ignores=[])