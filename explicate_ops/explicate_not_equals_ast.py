Module(
    body=[
        Assign(
            targets=[
                Name(id='t1073', ctx=Store())],
            value=Name(id='t12', ctx=Load())),
        Assign(
            targets=[
                Name(id='t1075', ctx=Store())],
            value=Name(id='t18', ctx=Load())),
        Assign(
            targets=[
                Name(id='t1078', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t1073', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t1078', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t1079', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t1075', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t1079', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t1080', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t1073', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t1081', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t1075', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t1082', ctx=Store())],
                            value=Compare(
                                left=Name(id='t1080', ctx=Load()),
                                ops=[
                                    NotEq()],
                                comparators=[
                                    Name(id='t1081', ctx=Load())])),
                        Assign(
                            targets=[
                                Name(id='t19', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_bool', ctx=Load()),
                                args=[
                                    Name(id='t1082', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t1083', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t1075', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t1083', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t1084', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t1073', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t1085', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t1075', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t1086', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t1084', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t1085', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t19', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t1086', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t1087', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t1073', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t1088', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t1075', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t1089', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t1087', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t1088', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t19', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t1089', ctx=Load())],
                                        keywords=[]))])])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t1090', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t1073', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t1090', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t1091', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t1075', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t1091', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t1092', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t1073', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t1093', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t1075', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t1094', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t1092', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t1093', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t19', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t1094', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t1095', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t1075', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t1095', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t1096', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t1073', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t1097', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t1075', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t1098', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t1096', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t1097', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t19', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t1098', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t1099', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t1073', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t1100', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t1075', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t1101', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t1099', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t1100', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t19', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t1101', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t1102', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t1075', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t1102', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t1103', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t1073', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t1104', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t1075', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t1105', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t1103', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t1104', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t19', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t1105', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t1106', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t1075', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t1106', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t1107', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t1073', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t1108', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t1075', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t1109', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t1107', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t1108', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t19', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t1109', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t1110', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t1073', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t1111', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t1075', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t1112', ctx=Store())],
                                            value=Call(
                                                func=Name(id='not_equal', ctx=Load()),
                                                args=[
                                                    Name(id='t1110', ctx=Load()),
                                                    Name(id='t1111', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t19', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t1112', ctx=Load())],
                                                keywords=[]))])])])])],
    type_ignores=[])