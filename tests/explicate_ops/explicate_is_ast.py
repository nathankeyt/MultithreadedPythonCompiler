Module(
    body=[
        Assign(
            targets=[
                Name(id='t6', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t8', ctx=Store())],
            value=Name(id='t1', ctx=Load())),
        Assign(
            targets=[
                Name(id='t11', ctx=Store())],
            value=Compare(
                left=Name(id='t6', ctx=Load()),
                ops=[
                    Eq()],
                comparators=[
                    Name(id='t8', ctx=Load())])),
        Assign(
            targets=[
                Name(id='t2', ctx=Store())],
            value=Call(
                func=Name(id='inject_bool', ctx=Load()),
                args=[
                    Name(id='t11', ctx=Load())],
                keywords=[]))],
    type_ignores=[])