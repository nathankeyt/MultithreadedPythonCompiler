Module(
    body=[
        Assign(
            targets=[
                Name(id='t8', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t10', ctx=Store())],
            value=Name(id='t1', ctx=Load())),
        Assign(
            targets=[
                Name(id='t13', ctx=Store())],
            value=Call(
                func=Name(id='is_true', ctx=Load()),
                args=[
                    Name(id='t10', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t13', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t14', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t8', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t14', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t3', ctx=Store())],
                            value=Name(id='t10', ctx=Load()))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t3', ctx=Store())],
                            value=Name(id='t8', ctx=Load()))])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t15', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t8', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t15', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t3', ctx=Store())],
                            value=Name(id='t10', ctx=Load()))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t3', ctx=Store())],
                            value=Name(id='t8', ctx=Load()))])])],
    type_ignores=[])