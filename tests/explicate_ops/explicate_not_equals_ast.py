Module(
    body=[
        Assign(
            targets=[
                Name(id='t83', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t85', ctx=Store())],
            value=Name(id='t1', ctx=Load())),
        Assign(
            targets=[
                Name(id='t88', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t83', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t88', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t89', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t85', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t89', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t90', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t83', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t91', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t85', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t92', ctx=Store())],
                            value=Compare(
                                left=Name(id='t90', ctx=Load()),
                                ops=[
                                    NotEq()],
                                comparators=[
                                    Name(id='t91', ctx=Load())])),
                        Assign(
                            targets=[
                                Name(id='t2', ctx=Store())],
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
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t85', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t93', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t94', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t83', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t95', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t85', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t96', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t94', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t95', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t96', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t97', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t83', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t98', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t85', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t99', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t97', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t98', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t99', ctx=Load())],
                                        keywords=[]))])])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t100', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t83', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t100', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t101', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t85', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t101', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t102', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t83', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t103', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t85', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t104', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t102', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t103', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t104', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t105', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t85', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t105', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t106', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t83', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t107', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t85', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t108', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t106', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t107', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t108', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t109', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t83', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t110', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t85', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t111', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t109', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t110', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t111', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t112', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t85', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t112', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t113', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t83', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t114', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t85', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t115', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t113', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t114', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t115', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t116', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t85', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t116', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t117', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t83', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t118', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t85', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t119', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t117', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t118', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t119', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t120', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t83', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t121', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t85', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t122', ctx=Store())],
                                            value=Call(
                                                func=Name(id='not_equal', ctx=Load()),
                                                args=[
                                                    Name(id='t120', ctx=Load()),
                                                    Name(id='t121', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t2', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t122', ctx=Load())],
                                                keywords=[]))])])])])],
    type_ignores=[])