Module(
    body=[
        Assign(
            targets=[
                Name(id='t210', ctx=Store())],
            value=Name(id='t6', ctx=Load())),
        Assign(
            targets=[
                Name(id='t212', ctx=Store())],
            value=Name(id='t8', ctx=Load())),
        Assign(
            targets=[
                Name(id='t215', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t210', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t215', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t216', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t212', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t216', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t217', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t210', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t218', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t212', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t219', ctx=Store())],
                            value=Compare(
                                left=Name(id='t217', ctx=Load()),
                                ops=[
                                    NotEq()],
                                comparators=[
                                    Name(id='t218', ctx=Load())])),
                        Assign(
                            targets=[
                                Name(id='t9', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_bool', ctx=Load()),
                                args=[
                                    Name(id='t219', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t220', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t212', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t220', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t221', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t210', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t222', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t212', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t223', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t221', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t222', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t9', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t223', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t224', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t210', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t225', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t212', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t226', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t224', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t225', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t9', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t226', ctx=Load())],
                                        keywords=[]))])])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t227', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t210', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t227', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t228', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t212', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t228', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t229', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t210', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t230', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t212', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t231', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t229', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t230', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t9', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t231', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t232', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t212', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t232', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t233', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t210', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t234', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t212', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t235', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t233', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t234', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t9', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t235', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t236', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t210', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t237', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t212', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t238', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t236', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t237', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t9', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t238', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t239', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t212', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t239', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t240', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t210', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t241', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t212', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t242', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t240', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t241', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t9', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t242', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t243', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t212', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t243', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t244', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t210', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t245', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t212', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t246', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t244', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t245', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t9', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t246', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t247', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t210', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t248', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t212', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t249', ctx=Store())],
                                            value=Call(
                                                func=Name(id='not_equal', ctx=Load()),
                                                args=[
                                                    Name(id='t247', ctx=Load()),
                                                    Name(id='t248', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t9', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t249', ctx=Load())],
                                                keywords=[]))])])])])],
    type_ignores=[])