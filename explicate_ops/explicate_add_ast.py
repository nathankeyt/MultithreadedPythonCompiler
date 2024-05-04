Module(
    body=[
        Assign(
            targets=[
                Name(id='t128', ctx=Store())],
            value=Name(id='t3', ctx=Load())),
        Assign(
            targets=[
                Name(id='t130', ctx=Store())],
            value=Name(id='t14', ctx=Load())),
        Assign(
            targets=[
                Name(id='t133', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t128', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t133', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t134', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t130', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t134', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t135', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t128', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t136', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t130', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t137', ctx=Store())],
                            value=BinOp(
                                left=Name(id='t135', ctx=Load()),
                                op=Add(),
                                right=Name(id='t136', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t3', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t137', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t138', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t130', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t138', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t139', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t128', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t140', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t130', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t141', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t139', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t140', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t3', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t141', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))])])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t142', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t128', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t142', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t143', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t130', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t143', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t144', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t128', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t145', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t130', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t146', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t144', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t145', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t3', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t146', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t147', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t130', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t147', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t148', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t128', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t149', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t130', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t150', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='t148', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='t149', ctx=Load()))),
                                        Assign(
                                            targets=[
                                                Name(id='t3', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_int', ctx=Load()),
                                                args=[
                                                    Name(id='t150', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='throw_type_error', ctx=Load()),
                                                args=[],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t151', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t130', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t151', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[]),
                        Assign(
                            targets=[
                                Name(id='t152', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t130', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t152', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t153', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_big', ctx=Load()),
                                        args=[
                                            Name(id='t130', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t153', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t154', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t128', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t155', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t130', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t156', ctx=Store())],
                                            value=Call(
                                                func=Name(id='add', ctx=Load()),
                                                args=[
                                                    Name(id='t154', ctx=Load()),
                                                    Name(id='t155', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t3', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_big', ctx=Load()),
                                                args=[
                                                    Name(id='t156', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[])])])])],
    type_ignores=[])