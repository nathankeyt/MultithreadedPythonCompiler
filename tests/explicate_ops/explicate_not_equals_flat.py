t473 = t6
t475 = t15
t478 = is_int(t473)
if t478:
    t479 = is_int(t475)
    if t479:
        t480 = project_int(t473)
        t481 = project_int(t475)
        t482 = t480 != t481
        t16 = inject_bool(t482)
    else:
        t483 = is_bool(t475)
        if t483:
            t484 = project_int(t473)
            t485 = project_bool(t475)
            t486 = t484 != t485
            t16 = inject_bool(t486)
        else:
            t487 = project_int(t473)
            t488 = project_big(t475)
            t489 = t487 != t488
            t16 = inject_bool(t489)
else:
    t490 = is_bool(t473)
    if t490:
        t491 = is_int(t475)
        if t491:
            t492 = project_bool(t473)
            t493 = project_int(t475)
            t494 = t492 != t493
            t16 = inject_bool(t494)
        else:
            t495 = is_bool(t475)
            if t495:
                t496 = project_bool(t473)
                t497 = project_bool(t475)
                t498 = t496 != t497
                t16 = inject_bool(t498)
            else:
                t499 = project_bool(t473)
                t500 = project_big(t475)
                t501 = t499 != t500
                t16 = inject_bool(t501)
    else:
        t502 = is_int(t475)
        if t502:
            t503 = project_big(t473)
            t504 = project_int(t475)
            t505 = t503 != t504
            t16 = inject_bool(t505)
        else:
            t506 = is_bool(t475)
            if t506:
                t507 = project_big(t473)
                t508 = project_bool(t475)
                t509 = t507 != t508
                t16 = inject_bool(t509)
            else:
                t510 = project_big(t473)
                t511 = project_big(t475)
                t512 = not_equal(t510, t511)
                t16 = inject_bool(t512)