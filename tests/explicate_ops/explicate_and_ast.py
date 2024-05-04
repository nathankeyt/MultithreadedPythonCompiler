Module(
    body=[
        Assign(
            targets=[
                Name(id='t683', ctx=Store())],
            value=Name(id='t13', ctx=Load())),
        Assign(
            targets=[
                Name(id='t685', ctx=Store())],
            value=Name(id='t15', ctx=Load())),
        Assign(
            targets=[
                Name(id='t688', ctx=Store())],
            value=Call(
                func=Name(id='is_true', ctx=Load()),
                args=[
                    Name(id='t685', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t688', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t689', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t683', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t689', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t16', ctx=Store())],
                            value=Name(id='t685', ctx=Load()))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t16', ctx=Store())],
                            value=Name(id='t683', ctx=Load()))])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t690', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t683', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t690', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t16', ctx=Store())],
                            value=Name(id='t685', ctx=Load()))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t16', ctx=Store())],
                            value=Name(id='t683', ctx=Load()))])])],
    type_ignores=[])