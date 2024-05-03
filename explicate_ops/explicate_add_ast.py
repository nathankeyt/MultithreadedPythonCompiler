Module(
    body=[
        Assign(
            targets=[
                Name(id='t72', ctx=Store())],
            value=Name(id='t26', ctx=Load())),
        Assign(
            targets=[
                Name(id='t74', ctx=Store())],
            value=Name(id='t7', ctx=Load())),
        Assign(
            targets=[
                Name(id='t77', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t72', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t77', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t78', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t74', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t78', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t79', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t72', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t80', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t74', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t81', ctx=Store())],
                            value=BinOp(
                                left=Name(id='t79', ctx=Load()),
                                op=Add(),
                                right=Name(id='t80', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t27', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t81', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t82', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t74', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t82', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t83', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t72', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t84', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t74', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t85', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t83', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t84', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t27', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t85', ctx=Load())],
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
                        Name(id='t86', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t72', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t86', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t87', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t74', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t87', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t88', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t72', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t89', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t74', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t90', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t88', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t89', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t27', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t90', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t91', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t74', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t91', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t92', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t72', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t93', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t74', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t94', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='t92', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='t93', ctx=Load()))),
                                        Assign(
                                            targets=[
                                                Name(id='t27', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_int', ctx=Load()),
                                                args=[
                                                    Name(id='t94', ctx=Load())],
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
                                Name(id='t95', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t74', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t95', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[]),
                        Assign(
                            targets=[
                                Name(id='t96', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t74', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t96', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t97', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_big', ctx=Load()),
                                        args=[
                                            Name(id='t74', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t97', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t98', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t72', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t99', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t74', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t100', ctx=Store())],
                                            value=Call(
                                                func=Name(id='add', ctx=Load()),
                                                args=[
                                                    Name(id='t98', ctx=Load()),
                                                    Name(id='t99', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t27', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_big', ctx=Load()),
                                                args=[
                                                    Name(id='t100', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[])])])])],
    type_ignores=[])