Module(
    body=[
        Assign(
            targets=[
                Name(id='t181', ctx=Store())],
            value=Name(id='t6', ctx=Load())),
        Assign(
            targets=[
                Name(id='t183', ctx=Store())],
            value=Name(id='t17', ctx=Load())),
        Assign(
            targets=[
                Name(id='t186', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t181', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t186', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t187', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t183', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t187', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t188', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t181', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t189', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t183', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t190', ctx=Store())],
                            value=BinOp(
                                left=Name(id='t188', ctx=Load()),
                                op=Add(),
                                right=Name(id='t189', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t6', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t190', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t191', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t183', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t191', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t192', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t181', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t193', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t183', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t194', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t192', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t193', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t194', ctx=Load())],
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
                        Name(id='t195', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t181', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t195', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t196', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t183', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t196', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t197', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t181', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t198', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t183', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t199', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t197', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t198', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t199', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t200', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t183', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t200', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t201', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t181', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t202', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t183', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t203', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='t201', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='t202', ctx=Load()))),
                                        Assign(
                                            targets=[
                                                Name(id='t6', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_int', ctx=Load()),
                                                args=[
                                                    Name(id='t203', ctx=Load())],
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
                                Name(id='t204', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t183', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t204', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[]),
                        Assign(
                            targets=[
                                Name(id='t205', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t183', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t205', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t206', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_big', ctx=Load()),
                                        args=[
                                            Name(id='t183', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t206', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t207', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t181', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t208', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t183', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t209', ctx=Store())],
                                            value=Call(
                                                func=Name(id='add', ctx=Load()),
                                                args=[
                                                    Name(id='t207', ctx=Load()),
                                                    Name(id='t208', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t6', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_big', ctx=Load()),
                                                args=[
                                                    Name(id='t209', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[])])])])],
    type_ignores=[])