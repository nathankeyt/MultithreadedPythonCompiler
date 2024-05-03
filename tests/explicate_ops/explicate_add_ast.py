Module(
    body=[
        Assign(
            targets=[
                Name(id='t596', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t598', ctx=Store())],
            value=Name(id='t41', ctx=Load())),
        Assign(
            targets=[
                Name(id='t601', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t596', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t601', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t602', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t598', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t602', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t603', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t596', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t604', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t598', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t605', ctx=Store())],
                            value=BinOp(
                                left=Name(id='t603', ctx=Load()),
                                op=Add(),
                                right=Name(id='t604', ctx=Load()))),
                        Assign(
                            targets=[
                                Name(id='t0', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_int', ctx=Load()),
                                args=[
                                    Name(id='t605', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t606', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t598', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t606', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t607', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t596', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t608', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t598', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t609', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t607', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t608', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t0', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t609', ctx=Load())],
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
                        Name(id='t610', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t596', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t610', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t611', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t598', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t611', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t612', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t596', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t613', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t598', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t614', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='t612', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='t613', ctx=Load()))),
                                Assign(
                                    targets=[
                                        Name(id='t0', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_int', ctx=Load()),
                                        args=[
                                            Name(id='t614', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t615', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t598', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t615', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t616', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t596', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t617', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t598', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t618', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='t616', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='t617', ctx=Load()))),
                                        Assign(
                                            targets=[
                                                Name(id='t0', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_int', ctx=Load()),
                                                args=[
                                                    Name(id='t618', ctx=Load())],
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
                                Name(id='t619', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t598', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t619', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[]),
                        Assign(
                            targets=[
                                Name(id='t620', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t598', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t620', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='throw_type_error', ctx=Load()),
                                        args=[],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t621', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_big', ctx=Load()),
                                        args=[
                                            Name(id='t598', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t621', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t622', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t596', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t623', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t598', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t624', ctx=Store())],
                                            value=Call(
                                                func=Name(id='add', ctx=Load()),
                                                args=[
                                                    Name(id='t622', ctx=Load()),
                                                    Name(id='t623', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t0', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_big', ctx=Load()),
                                                args=[
                                                    Name(id='t624', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[])])])])],
    type_ignores=[])