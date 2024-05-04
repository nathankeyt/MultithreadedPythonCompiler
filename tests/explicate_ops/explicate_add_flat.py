t596 = t0
t598 = t41
t601 = is_int(t596)
if t601:
    t602 = is_int(t598)
    if t602:
        t603 = project_int(t596)
        t604 = project_int(t598)
        t605 = t603 + t604
        t0 = inject_int(t605)
    else:
        t606 = is_bool(t598)
        if t606:
            t607 = project_int(t596)
            t608 = project_bool(t598)
            t609 = t607 + t608
            t0 = inject_int(t609)
        else:
            throw_type_error()
else:
    t610 = is_bool(t596)
    if t610:
        t611 = is_int(t598)
        if t611:
            t612 = project_bool(t596)
            t613 = project_int(t598)
            t614 = t612 + t613
            t0 = inject_int(t614)
        else:
            t615 = is_bool(t598)
            if t615:
                t616 = project_bool(t596)
                t617 = project_bool(t598)
                t618 = t616 + t617
                t0 = inject_int(t618)
            else:
                throw_type_error()
    else:
        t619 = is_int(t598)
        if t619:
            throw_type_error()
        t620 = is_int(t598)
        if t620:
            throw_type_error()
        else:
            t621 = is_big(t598)
            if t621:
                t622 = project_big(t596)
                t623 = project_big(t598)
                t624 = add(t622, t623)
                t0 = inject_big(t624)