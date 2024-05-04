Module(
    body=[
        Assign(
            targets=[
                Name(id='t702', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t704', ctx=Store())],
            value=Name(id='t5', ctx=Load())),
        Assign(
            targets=[
                Name(id='t707', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t702', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t707', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t708', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t704', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t708', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t709', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t702', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t710', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t704', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t711', ctx=Store())],
                            value=Compare(
                                left=Name(id='t709', ctx=Load()),
                                ops=[
                                    NotEq()],
                                comparators=[
                                    Name(id='t710', ctx=Load())])),
                        Assign(
                            targets=[
                                Name(id='t6', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_bool', ctx=Load()),
                                args=[
                                    Name(id='t711', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t712', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t704', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t712', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t713', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t702', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t714', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t704', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t715', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t713', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t714', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t715', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t716', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t702', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t717', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t704', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t718', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t716', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t717', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t718', ctx=Load())],
                                        keywords=[]))])])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t719', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t702', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t719', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t720', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t704', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t720', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t721', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t702', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t722', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t704', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t723', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t721', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t722', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t723', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t724', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t704', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t724', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t725', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t702', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t726', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t704', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t727', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t725', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t726', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t6', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t727', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t728', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t702', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t729', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t704', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t730', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t728', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t729', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t6', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t730', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t731', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t704', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t731', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t732', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t702', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t733', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t704', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t734', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t732', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t733', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t6', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t734', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t735', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t704', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t735', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t736', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t702', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t737', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t704', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t738', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t736', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t737', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t6', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t738', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t739', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t702', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t740', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t704', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t741', ctx=Store())],
                                            value=Call(
                                                func=Name(id='not_equal', ctx=Load()),
                                                args=[
                                                    Name(id='t739', ctx=Load()),
                                                    Name(id='t740', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t6', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t741', ctx=Load())],
                                                keywords=[]))])])])])],
    type_ignores=[])