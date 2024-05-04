Module(
    body=[
        Assign(
            targets=[
                Name(id='t157', ctx=Store())],
            value=Name(id='t1', ctx=Load())),
        Assign(
            targets=[
                Name(id='t159', ctx=Store())],
            value=Name(id='t8', ctx=Load())),
        Assign(
            targets=[
                Name(id='t162', ctx=Store())],
            value=Call(
                func=Name(id='is_int', ctx=Load()),
                args=[
                    Name(id='t157', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t162', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t163', ctx=Store())],
                    value=Call(
                        func=Name(id='is_int', ctx=Load()),
                        args=[
                            Name(id='t159', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t163', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t164', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t157', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t165', ctx=Store())],
                            value=Call(
                                func=Name(id='project_int', ctx=Load()),
                                args=[
                                    Name(id='t159', ctx=Load())],
                                keywords=[])),
                        Assign(
                            targets=[
                                Name(id='t166', ctx=Store())],
                            value=Compare(
                                left=Name(id='t164', ctx=Load()),
                                ops=[
                                    NotEq()],
                                comparators=[
                                    Name(id='t165', ctx=Load())])),
                        Assign(
                            targets=[
                                Name(id='t9', ctx=Store())],
                            value=Call(
                                func=Name(id='inject_bool', ctx=Load()),
                                args=[
                                    Name(id='t166', ctx=Load())],
                                keywords=[]))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t167', ctx=Store())],
                            value=Call(
                                func=Name(id='is_bool', ctx=Load()),
                                args=[
                                    Name(id='t159', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t167', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t168', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t157', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t169', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t159', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t170', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t168', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t169', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t9', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t170', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t171', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t157', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t172', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t159', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t173', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t171', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t172', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t9', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t173', ctx=Load())],
                                        keywords=[]))])])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t174', ctx=Store())],
                    value=Call(
                        func=Name(id='is_bool', ctx=Load()),
                        args=[
                            Name(id='t157', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t174', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t175', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t159', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t175', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t176', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_bool', ctx=Load()),
                                        args=[
                                            Name(id='t157', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t177', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t159', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t178', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t176', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t177', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t9', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t178', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t179', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t159', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t179', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t180', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t157', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t181', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t159', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t182', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t180', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t181', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t9', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t182', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t183', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t157', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t184', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t159', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t185', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t183', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t184', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t9', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t185', ctx=Load())],
                                                keywords=[]))])])],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t186', ctx=Store())],
                            value=Call(
                                func=Name(id='is_int', ctx=Load()),
                                args=[
                                    Name(id='t159', ctx=Load())],
                                keywords=[])),
                        If(
                            test=Name(id='t186', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Name(id='t187', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_big', ctx=Load()),
                                        args=[
                                            Name(id='t157', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t188', ctx=Store())],
                                    value=Call(
                                        func=Name(id='project_int', ctx=Load()),
                                        args=[
                                            Name(id='t159', ctx=Load())],
                                        keywords=[])),
                                Assign(
                                    targets=[
                                        Name(id='t189', ctx=Store())],
                                    value=Compare(
                                        left=Name(id='t187', ctx=Load()),
                                        ops=[
                                            NotEq()],
                                        comparators=[
                                            Name(id='t188', ctx=Load())])),
                                Assign(
                                    targets=[
                                        Name(id='t9', ctx=Store())],
                                    value=Call(
                                        func=Name(id='inject_bool', ctx=Load()),
                                        args=[
                                            Name(id='t189', ctx=Load())],
                                        keywords=[]))],
                            orelse=[
                                Assign(
                                    targets=[
                                        Name(id='t190', ctx=Store())],
                                    value=Call(
                                        func=Name(id='is_bool', ctx=Load()),
                                        args=[
                                            Name(id='t159', ctx=Load())],
                                        keywords=[])),
                                If(
                                    test=Name(id='t190', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Name(id='t191', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t157', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t192', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t159', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t193', ctx=Store())],
                                            value=Compare(
                                                left=Name(id='t191', ctx=Load()),
                                                ops=[
                                                    NotEq()],
                                                comparators=[
                                                    Name(id='t192', ctx=Load())])),
                                        Assign(
                                            targets=[
                                                Name(id='t9', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t193', ctx=Load())],
                                                keywords=[]))],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Name(id='t194', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t157', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t195', ctx=Store())],
                                            value=Call(
                                                func=Name(id='project_big', ctx=Load()),
                                                args=[
                                                    Name(id='t159', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t196', ctx=Store())],
                                            value=Call(
                                                func=Name(id='not_equal', ctx=Load()),
                                                args=[
                                                    Name(id='t194', ctx=Load()),
                                                    Name(id='t195', ctx=Load())],
                                                keywords=[])),
                                        Assign(
                                            targets=[
                                                Name(id='t9', ctx=Store())],
                                            value=Call(
                                                func=Name(id='inject_bool', ctx=Load()),
                                                args=[
                                                    Name(id='t196', ctx=Load())],
                                                keywords=[]))])])])])],
    type_ignores=[])