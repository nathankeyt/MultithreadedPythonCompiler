# a = b and c expands to
tmp0 = b # tmp var for let
tmp1 = c # tmp var for let

if is_true(tmp1):
    if is_true(tmp0):
        a = tmp1
    else:
        a = tmp0
else:
    if is_true(tmp0):
        a = tmp1
    else:
        a = tmp0