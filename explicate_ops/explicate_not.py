# a = not b expands to
tmp0 = b # tmp var for let

if (is_true(tmp0)):  
    a = inject_bool(0)
else:
    a = inject_bool(1)