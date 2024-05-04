t453 = t0
t455 = t33
t458 = is_int(t453)
if t458:
    t459 = is_int(t455)
    if t459:
        t460 = project_int(t453)
        t461 = project_int(t455)
        t462 = t460 == t461
        t34 = inject_bool(t462)
    else:
        t463 = is_bool(t455)
        if t463:
            t464 = project_int(t453)
            t465 = project_bool(t455)
            t466 = t464 == t465
            t34 = inject_bool(t466)
        else:
            t467 = project_int(t453)
            t468 = project_big(t455)
            t469 = t467 == t468
            t34 = inject_bool(t469)
else:
    t470 = is_bool(t453)
    if t470:
        t471 = is_int(t455)
        if t471:
            t472 = project_bool(t453)
            t473 = project_int(t455)
            t474 = t472 == t473
            t34 = inject_bool(t474)
        else:
            t475 = is_bool(t455)
            if t475:
                t476 = project_bool(t453)
                t477 = project_bool(t455)
                t478 = t476 == t477
                t34 = inject_bool(t478)
            else:
                t479 = project_bool(t453)
                t480 = project_big(t455)
                t481 = t479 == t480
                t34 = inject_bool(t481)
    else:
        t482 = is_int(t455)
        if t482:
            t483 = project_big(t453)
            t484 = project_int(t455)
            t485 = t483 == t484
            t34 = inject_bool(t485)
        else:
            t486 = is_bool(t455)
            if t486:
                t487 = project_big(t453)
                t488 = project_bool(t455)
                t489 = t487 == t488
                t34 = inject_bool(t489)
            else:
                t490 = project_big(t453)
                t491 = project_big(t455)
                t492 = equal(t490, t491)
                t34 = inject_bool(t492)