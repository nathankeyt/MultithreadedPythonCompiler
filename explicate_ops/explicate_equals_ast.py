Module(
    body=[
        Assign(
            targets=[
                Name(id='t839', ctx=Store())],
            value=Name(id='t12', ctx=Load())),
        Assign(
            targets=[
                Name(id='t841', ctx=Store())],
            value=Name(id='t22', ctx=Load())),
        Assign(
            targets=[
                Name(id='t844', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t839', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t844', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t845', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t841', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t845', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t846', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t839', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t847', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t841', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t848', ctx=Store())],
                            value=Compare(
                                left=Name(id='t846', ctx=Load()),
                                ops=[
                                    Eq()],
                                comparators=[
                                    Name(id='t847', ctx=Load())])),
                        Assign(
                            targets=[
                                Name(id='t23', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_bool', ctx=Load()),
                                args=[
                                    Name(id='t848', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t849', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t841', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t849', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t850', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t839', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t851', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t841', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t852', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t850', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t851', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t23', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t852', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t853', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t839', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t854', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t841', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t855', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t853', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t854', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t23', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t855', ctx=Load())],
                                        keywords=[]))])])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t856', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t839', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t856', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t857', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t841', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t857', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t858', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t839', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t859', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t841', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t860', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t858', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t859', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t23', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t860', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t861', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t841', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t861', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t862', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t839', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t863', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t841', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t864', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t862', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t863', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t23', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t864', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t865', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t839', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t866', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t841', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t867', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t865', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t866', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t23', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t867', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t868', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t841', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t868', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t869', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t839', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t870', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t841', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t871', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t869', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t870', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t23', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t871', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t872', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t841', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t872', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t873', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t839', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t874', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t841', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t875', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t873', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t874', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t23', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t875', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t876', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t839', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t877', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t841', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t878', ctx=Store())],
                                            value=Call(
                                                func=Name(id='equal', ctx=Load()),
                                                args=[
                                                    Name(id='t876', ctx=Load()),
                                                    Name(id='t877', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t23', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t878', ctx=Load())],
                                                keywords=[]))])])])])],
    type_ignores=[])