Module(
    body=[
        Assign(
            targets=[
                Name(id='t94', ctx=Store())],
            value=Name(id='t6', ctx=Load())),
        Assign(
            targets=[
                Name(id='t96', ctx=Store())],
            value=Name(id='t11', ctx=Load())),
        Assign(
            targets=[
                Name(id='t99', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t94', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t99', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t100', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t96', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t100', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t101', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t94', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t102', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t96', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t103', ctx=Store())],
                            value=Compare(
                                left=Name(id='t101', ctx=Load()),
                                ops=[
                                    Eq()],
                                comparators=[
                                    Name(id='t102', ctx=Load())])),
                        Assign(
                            targets=[
                                Name(id='t12', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_bool', ctx=Load()),
                                args=[
                                    Name(id='t103', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t104', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t96', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t104', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t105', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t94', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t106', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t96', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t107', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t105', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t106', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t12', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t107', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t108', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t94', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t109', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t96', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t110', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t108', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t109', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t12', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t110', ctx=Load())],
                                        keywords=[]))])])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t111', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t94', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t111', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t112', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t96', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t112', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t113', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t94', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t114', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t96', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t115', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t113', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t114', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t12', ctx=Store())],
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
                                            Name(id='t96', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t116', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t117', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t94', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t118', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t96', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t119', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t117', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t118', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t12', ctx=Store())],
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
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t94', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t121', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t96', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t122', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t120', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t121', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t12', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t122', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t123', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t96', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t123', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t124', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t94', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t125', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t96', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t126', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t124', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t125', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t12', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t126', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t127', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t96', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t127', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t128', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t94', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t129', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t96', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t130', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t128', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t129', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t12', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t130', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t131', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t94', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t132', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t96', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t133', ctx=Store())],
                                            value=Call(
                                                func=Name(id='equal', ctx=Load()),
                                                args=[
                                                    Name(id='t131', ctx=Load()),
                                                    Name(id='t132', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t12', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t133', ctx=Load())],
                                                keywords=[]))])])])])],
    type_ignores=[])