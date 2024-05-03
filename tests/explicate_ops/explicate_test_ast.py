Module(
    body=[
        Assign(
            targets=[
                Name(id='t49', ctx=Store())],
            value=Name(id='t2', ctx=Load())),
        Assign(
            targets=[
                Name(id='t52', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t49', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t52', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t48', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t49', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t53', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t49', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t53', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t48', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t49', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t54', ctx=Store())],
                            value=Call(
                                func=Name(id='is_big', ctx=Load()),
                                args=[
                                    Name(id='t49', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t54', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t48', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t49', ctx=Load())],
                                        keywords=[]))],
                            orelse=[])])])],
    type_ignores=[])