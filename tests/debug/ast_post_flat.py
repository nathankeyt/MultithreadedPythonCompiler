Module(
    body=[
        Assign(
            targets=[
                Name(id='t0', ctx=Store())],
            value=Call(
                func=Name(id='inject_int', ctx=Load()),
                args=[
                    Constant(value=1)],
                keywords=[])),
        Assign(
            targets=[
                Name(id='t1', ctx=Store())],
            value=Call(
                func=Name(id='inject_int', ctx=Load()),
                args=[
                    Constant(value=100)],
                keywords=[])),
        Assign(
            targets=[
                Name(id='t2', ctx=Store())],
            value=Compare(
                left=Name(id='t0', ctx=Load()),
                ops=[
                    NotEq()],
                comparators=[
                    Name(id='t1', ctx=Load())])),
        Assign(
            targets=[
                Name(id='t3', ctx=Store())],
            value=Call(
                func=Name(id='int', ctx=Load()),
                args=[
                    Name(id='t2', ctx=Load())],
                keywords=[])),
        Assign(
            targets=[
                Name(id='t4', ctx=Store())],
            value=Call(
                func=Name(id='is_true', ctx=Load()),
                args=[
                    Name(id='t3', ctx=Load())],
                keywords=[])),
        While(
            test=Name(id='t4', ctx=Load()),
            body=[
                Assign(
                    targets=[
                        Name(id='t5', ctx=Store())],
                    value=Call(
                        func=Name(id='inject_int', ctx=Load()),
                        args=[
                            Constant(value=1)],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t0', ctx=Store())],
                    value=BinOp(
                        left=Name(id='t0', ctx=Load()),
                        op=Add(),
                        right=Name(id='t5', ctx=Load()))),
                Assign(
                    targets=[
                        Name(id='t6', ctx=Store())],
                    value=BoolOp(
                        op=And(),
                        values=[
                            Name(id='t0', ctx=Load()),
                            Name(id='t1', ctx=Load())])),
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            Name(id='t6', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t2', ctx=Store())],
                    value=Compare(
                        left=Name(id='t0', ctx=Load()),
                        ops=[
                            NotEq()],
                        comparators=[
                            Name(id='t1', ctx=Load())])),
                Assign(
                    targets=[
                        Name(id='t3', ctx=Store())],
                    value=Call(
                        func=Name(id='int', ctx=Load()),
                        args=[
                            Name(id='t2', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='t4', ctx=Store())],
                    value=Call(
                        func=Name(id='is_true', ctx=Load()),
                        args=[
                            Name(id='t3', ctx=Load())],
                        keywords=[]))],
            orelse=[])],
    type_ignores=[])