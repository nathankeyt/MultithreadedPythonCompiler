t558 = t39
t561 = is_int(t558)
if t561:
    t562 = project_int(t558)
    t563 = -t562
    t40 = inject_int(t563)
else:
    t564 = is_bool(t558)
    if t564:
        t565 = project_bool(t558)
        t566 = -t565
        t40 = inject_int(t566)
    else:
        throw_type_error()