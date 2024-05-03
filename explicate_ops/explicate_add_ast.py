Module(
    body=[
        Assign(
            targets=[
                Name(id='t1044', ctx=Store())],
            value=Name(id='t12', ctx=Load())),
        Assign(
            targets=[
                Name(id='t1046', ctx=Store())],
            value=Name(id='t33', ctx=Load())),
        Assign(
            targets=[
                Name(id='t1049', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t1044', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t1049', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t1050', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t1046', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t1050', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t1051', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t1044', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t1052', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t1046', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t1053', ctx=Store())],
                            value=BinOp(
                                left=Name(id='t1051', ctx=Load()),
                                op=Add(),
                                right=Name(id='t1052', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t12', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t1053', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t1054', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t1046', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t1054', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t1055', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t1044', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t1056', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t1046', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t1057', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t1055', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t1056', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t12', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t1057', ctx=Load())],
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
                        Name(id='t1058', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t1044', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t1058', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t1059', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t1046', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t1059', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t1060', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t1044', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t1061', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t1046', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t1062', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t1060', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t1061', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t12', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t1062', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t1063', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t1046', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t1063', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t1064', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t1044', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t1065', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t1046', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t1066', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='t1064', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='t1065', ctx=Load()))),
                                        Assign(
                                            targets=[
                                                Name(id='t12', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_int', ctx=Load()),
                                                args=[
                                                    Name(id='t1066', ctx=Load())],
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
                                Name(id='t1067', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t1046', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t1067', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[]),
                        Assign(
                            targets=[
                                Name(id='t1068', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t1046', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t1068', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t1069', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_big', ctx=Load()),
                                        args=[
                                            Name(id='t1046', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t1069', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t1070', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t1044', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t1071', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t1046', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t1072', ctx=Store())],
                                            value=Call(
                                                func=Name(id='add', ctx=Load()),
                                                args=[
                                                    Name(id='t1070', ctx=Load()),
                                                    Name(id='t1071', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t12', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_big', ctx=Load()),
                                                args=[
                                                    Name(id='t1072', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[])])])])],
    type_ignores=[])