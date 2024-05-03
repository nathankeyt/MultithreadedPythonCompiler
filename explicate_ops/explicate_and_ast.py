Module(
    body=[
        Assign(
            targets=[
                Name(id='t97', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t99', ctx=Store())],
            value=Name(id='t1', ctx=Load())),
        Assign(
            targets=[
                Name(id='t102', ctx=Store())],
            value=Call(
                func=Name(id='is_true', ctx=Load()),
                args=[
                    Name(id='t99', ctx=Load())],
                keywords=[])),
        If(
            test=Name(id='t102', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t103', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t97', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t103', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t5', ctx=Store())],
                            value=Name(id='t99', ctx=Load()))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t5', ctx=Store())],
                            value=Name(id='t97', ctx=Load()))])],
            orelse=[
                Assign(
                    targets=[
                        Name(id='t104', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t97', ctx=Load())],
                        keywords=[])),
                If(
                    test=Name(id='t104', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Name(id='t5', ctx=Store())],
                            value=Name(id='t99', ctx=Load()))],
                    orelse=[
                        Assign(
                            targets=[
                                Name(id='t5', ctx=Store())],
                            value=Name(id='t97', ctx=Load()))])])],
    type_ignores=[])