# a = b or c expands to
tmp0 = b # tmp var for let
tmp1 = c # tmp var for let

if is_true(tmp0):
    a = tmp0
else:
    a = tmp1
