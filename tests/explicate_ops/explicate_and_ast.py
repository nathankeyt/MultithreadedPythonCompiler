Module(
    body=[
        Assign(
            targets=[
                Name(id='t103', ctx=Store())],
            value=Name(id='t3', ctx=Load())),
        Assign(
            targets=[
                Name(id='t105', ctx=Store())],
            value=Name(id='t7', ctx=Load())),
        Assign(
            targets=[
                Name(id='t108', ctx=Store())],
            value=Call(
                func=Name(id='is_true', ctx=Load()),
                args=[
                    Name(id='t105', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t108', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t109', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t103', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t109', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t8', ctx=Store())],
                            value=Name(id='t105', ctx=Load()))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t8', ctx=Store())],
                            value=Name(id='t103', ctx=Load()))])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t110', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t103', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t110', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t8', ctx=Store())],
                            value=Name(id='t105', ctx=Load()))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t8', ctx=Store())],
                            value=Name(id='t103', ctx=Load()))])])],
    type_ignores=[])