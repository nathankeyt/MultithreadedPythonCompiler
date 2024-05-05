Module(
    body=[
        Assign(
            targets=[
                Name(id='t957', ctx=Store())],
            value=Name(id='t5', ctx=Load())),
        Assign(
            targets=[
                Name(id='t960', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t957', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t960', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t961', ctx=Store())],
                    value=Call(
                        func=Name(id='project_int', ctx=Load()),
                        args=[
                            Name(id='t957', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t6', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Name(id='t961', ctx=Load())],
                        keywords=[]))],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t962', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t957', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t962', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t963', ctx=Store())],
                            value=Call(
                                func=Name(id='project_bool', ctx=Load()),
                                args=[
                                    Name(id='t957', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t6', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t963', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Expr(
                            value=Call(
                                func=Name(id='throw_type_error', ctx=Load()),
                                args=[],
                                keywords=[]))])])],
    type_ignores=[])