Module(
    body=[
        Assign(
            targets=[
                Name(id='t116', ctx=Store())],
            value=Name(id='t2', ctx=Load())),
        Assign(
            targets=[
                Name(id='t118', ctx=Store())],
            value=Name(id='t43', ctx=Load())),
        Assign(
            targets=[
                Name(id='t121', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t116', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t121', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t122', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t118', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t122', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t123', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t116', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t124', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t118', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t125', ctx=Store())],
                            value=Compare(
                                left=Name(id='t123', ctx=Load()),
                                ops=[
                                    Eq()],
                                comparators=[
                                    Name(id='t124', ctx=Load())])),
                        Assign(
                            targets=[
                                Name(id='t44', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_bool', ctx=Load()),
                                args=[
                                    Name(id='t125', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t126', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t118', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t126', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t127', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t116', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t128', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t118', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t129', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t127', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t128', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t44', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t129', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t130', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t116', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t131', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t118', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t132', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t130', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t131', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t44', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t132', ctx=Load())],
                                        keywords=[]))])])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t133', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t116', ctx=Load())],
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
                                    Name(id='t118', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t134', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t135', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t116', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t136', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t118', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t137', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t135', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t136', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t44', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
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
                                            Name(id='t118', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t138', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t139', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t116', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t140', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t118', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t141', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t139', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t140', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t44', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t141', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t142', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t116', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t143', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t118', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t144', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t142', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t143', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t44', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t144', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t145', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t118', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t145', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t146', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t116', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t147', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t118', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t148', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t146', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t147', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t44', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t148', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t149', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t118', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t149', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t150', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t116', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t151', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t118', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t152', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t150', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t151', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t44', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t152', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t153', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t116', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t154', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t118', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t155', ctx=Store())],
                                            value=Call(
                                                func=Name(id='equal', ctx=Load()),
                                                args=[
                                                    Name(id='t153', ctx=Load()),
                                                    Name(id='t154', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t44', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t155', ctx=Load())],
                                                keywords=[]))])])])])],
    type_ignores=[])