Module(
    body=[
        Assign(
            targets=[
                Name(id='t453', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t455', ctx=Store())],
            value=Name(id='t33', ctx=Load())),
        Assign(
            targets=[
                Name(id='t458', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t453', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t458', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t459', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t455', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t459', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t460', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t453', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t461', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t455', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t462', ctx=Store())],
                            value=Compare(
                                left=Name(id='t460', ctx=Load()),
                                ops=[
                                    Eq()],
                                comparators=[
                                    Name(id='t461', ctx=Load())])),
                        Assign(
                            targets=[
                                Name(id='t34', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_bool', ctx=Load()),
                                args=[
                                    Name(id='t462', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t463', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t455', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t463', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t464', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t453', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t465', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t455', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t466', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t464', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t465', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t34', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t466', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t467', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t453', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t468', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t455', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t469', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t467', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t468', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t34', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t469', ctx=Load())],
                                        keywords=[]))])])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t470', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t453', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t470', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t471', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t455', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t471', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t472', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t453', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t473', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t455', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t474', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t472', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t473', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t34', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t474', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t475', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t455', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t475', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t476', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t453', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t477', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t455', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t478', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t476', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t477', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t34', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t478', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t479', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t453', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t480', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t455', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t481', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t479', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t480', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t34', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t481', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t482', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t455', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t482', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t483', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t453', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t484', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t455', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t485', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t483', ctx=Load()),
                                        ops=[
                                            Eq()],
                                        comparators=[
                                            Name(id='t484', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t34', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t485', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t486', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t455', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t486', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t487', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t453', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t488', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t455', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t489', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t487', ctx=Load()),
                                                ops=[
                                                    Eq()],
                                                comparators=[
                                                    Name(id='t488', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t34', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t489', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t490', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t453', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t491', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t455', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t492', ctx=Store())],
                                            value=Call(
                                                func=Name(id='equal', ctx=Load()),
                                                args=[
                                                    Name(id='t490', ctx=Load()),
                                                    Name(id='t491', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t34', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t492', ctx=Load())],
                                                keywords=[]))])])])])],
    type_ignores=[])