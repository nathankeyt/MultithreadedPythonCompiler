Module(
    body=[
        Assign(
            targets=[
                Name(id='t54', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t56', ctx=Store())],
            value=Name(id='t5', ctx=Load())),
        Assign(
            targets=[
                Name(id='t59', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t54', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t59', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t60', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t56', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t60', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t61', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t54', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t62', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t56', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t63', ctx=Store())],
                            value=BinOp(
                                left=Name(id='t61', ctx=Load()),
                                op=Add(),
                                right=Name(id='t62', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t0', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t63', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t64', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t56', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t64', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t65', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t54', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t66', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t56', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t67', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t65', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t66', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t0', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t67', ctx=Load())],
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
                        Name(id='t68', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t54', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t68', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t69', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t56', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t69', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t70', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t54', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t71', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t56', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t72', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t70', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t71', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t0', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t72', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t73', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t56', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t73', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t74', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t54', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t75', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t56', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t76', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='t74', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='t75', ctx=Load()))),
                                        Assign(
                                            targets=[
                                                Name(id='t0', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_int', ctx=Load()),
                                                args=[
                                                    Name(id='t76', ctx=Load())],
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
                                Name(id='t77', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t56', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t77', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[]),
                        Assign(
                            targets=[
                                Name(id='t78', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t56', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t78', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t79', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_big', ctx=Load()),
                                        args=[
                                            Name(id='t56', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t79', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t80', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t54', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t81', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t56', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t82', ctx=Store())],
                                            value=Call(
                                                func=Name(id='add', ctx=Load()),
                                                args=[
                                                    Name(id='t80', ctx=Load()),
                                                    Name(id='t81', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t0', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_big', ctx=Load()),
                                                args=[
                                                    Name(id='t82', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[])])])])],
    type_ignores=[])