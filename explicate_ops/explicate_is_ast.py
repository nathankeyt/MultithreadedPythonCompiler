Module(
    body=[
        Assign(
            targets=[
                Name(id='t3', ctx=Store())],
            value=Name(id='t0', ctx=Load())),
        Assign(
            targets=[
                Name(id='t5', ctx=Store())],
            value=Name(id='t1', ctx=Load())),
        Assign(
            targets=[
                Name(id='t8', ctx=Store())],
            value=Compare(
                left=Name(id='t3', ctx=Load()),
                ops=[
                    Eq()],
                comparators=[
                    Name(id='t5', ctx=Load())])),
        Assign(
            targets=[
                Name(id='t2', ctx=Store())],
            value=Call(
                func=Name(id='inject_bool', ctx=Load()),
                args=[
                    Name(id='t8', ctx=Load())],
                keywords=[]))],
    type_ignores=[])