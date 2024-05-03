Module(
    body=[
        Assign(
            targets=[
                Name(id='t56', ctx=Store())],
            value=Name(id='t4', ctx=Load())),
        Assign(
            targets=[
                Name(id='t58', ctx=Store())],
            value=Name(id='t5', ctx=Load())),
        Assign(
            targets=[
                Name(id='t61', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t56', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t61', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t62', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t58', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t62', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t63', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t56', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t64', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t58', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t65', ctx=Store())],
                            value=Compare(
                                left=Name(id='t63', ctx=Load()),
                                ops=[
                                    Eq()],
                                comparators=[
                                    Name(id='t64', ctx=Load())])),
                        Assign(
                            targets=[
                                Name(id='t6', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_bool', ctx=Load()),
                                args=[
                                    Name(id='t65', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t66', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t58', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t66', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t67', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t56', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t68', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t58', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t69', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t67', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t68', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t69', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t70', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t56', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t71', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t58', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t72', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t70', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t71', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t72', ctx=Load())],
                                        keywords=[]))])])],
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
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t58', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t74', ctx=Load()),
                            body=[
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
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t58', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t77', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t75', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t76', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t77', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t78', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t58', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t78', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t79', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t56', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t80', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t58', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t81', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t79', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t80', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t6', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t81', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t82', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t56', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t83', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t58', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t84', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t82', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t83', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t6', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t84', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t85', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t58', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t85', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t86', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t56', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t87', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t58', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t88', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t86', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t87', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t88', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t89', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t58', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t89', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t90', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t56', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t91', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t58', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t92', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t90', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t91', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t6', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t92', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t93', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t56', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t94', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t58', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t95', ctx=Store())],
                                            value=Call(
                                                func=Name(id='equal', ctx=Load()),
                                                args=[
                                                    Name(id='t93', ctx=Load()),
                                                    Name(id='t94', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t6', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t95', ctx=Load())],
                                                keywords=[]))])])])])],
    type_ignores=[])