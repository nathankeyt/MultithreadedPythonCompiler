Module(
    body=[
        Assign(
            targets=[
                Name(id='t473', ctx=Store())],
            value=Name(id='t6', ctx=Load())),
        Assign(
            targets=[
                Name(id='t475', ctx=Store())],
            value=Name(id='t15', ctx=Load())),
        Assign(
            targets=[
                Name(id='t478', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t473', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t478', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t479', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t475', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t479', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t480', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t473', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t481', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t475', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t482', ctx=Store())],
                            value=Compare(
                                left=Name(id='t480', ctx=Load()),
                                ops=[
                                    NotEq()],
                                comparators=[
                                    Name(id='t481', ctx=Load())])),
                        Assign(
                            targets=[
                                Name(id='t16', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_bool', ctx=Load()),
                                args=[
                                    Name(id='t482', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t483', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t475', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t483', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t484', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t473', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t485', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t475', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t486', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t484', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t485', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t16', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t486', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t487', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t473', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t488', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t475', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t489', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t487', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t488', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t16', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t489', ctx=Load())],
                                        keywords=[]))])])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t490', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t473', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t490', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t491', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t475', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t491', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t492', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t473', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t493', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t475', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t494', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t492', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t493', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t16', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t494', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t495', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t475', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t495', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t496', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t473', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t497', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t475', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t498', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t496', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t497', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t16', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t498', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t499', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t473', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t500', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t475', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t501', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t499', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t500', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t16', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t501', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t502', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t475', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t502', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t503', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t473', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t504', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t475', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t505', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t503', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t504', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t16', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t505', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t506', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t475', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t506', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t507', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t473', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t508', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t475', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t509', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t507', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t508', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t16', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t509', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t510', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t473', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t511', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t475', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t512', ctx=Store())],
                                            value=Call(
                                                func=Name(id='not_equal', ctx=Load()),
                                                args=[
                                                    Name(id='t510', ctx=Load()),
                                                    Name(id='t511', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t16', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t512', ctx=Load())],
                                                keywords=[]))])])])])],
    type_ignores=[])