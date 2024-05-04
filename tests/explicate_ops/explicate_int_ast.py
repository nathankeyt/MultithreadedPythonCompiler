Module(
    body=[
        Assign(
            targets=[
                Name(id='t742', ctx=Store())],
            value=Name(id='t6', ctx=Load())),
        Assign(
            targets=[
                Name(id='t745', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t742', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t745', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t746', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t742', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t7', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t746', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t747', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t742', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t747', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t748', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t742', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t7', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t748', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])])],
    type_ignores=[])