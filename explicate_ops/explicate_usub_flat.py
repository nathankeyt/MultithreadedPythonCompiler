t435 = t13
t438 = is_int(t435)
if t438:
    t439 = project_int(t435)
    t440 = -t439
    t14 = inject_int(t440)
else:
    t441 = is_bool(t435)
    if t441:
        t442 = project_bool(t435)
        t443 = -t442
        t14 = inject_int(t443)
    else:
        throw_type_error()