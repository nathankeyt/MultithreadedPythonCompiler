t702 = t0
t704 = t5
t707 = is_int(t702)
if t707:
    t708 = is_int(t704)
    if t708:
        t709 = project_int(t702)
        t710 = project_int(t704)
        t711 = t709 != t710
        t6 = inject_bool(t711)
    else:
        t712 = is_bool(t704)
        if t712:
            t713 = project_int(t702)
            t714 = project_bool(t704)
            t715 = t713 != t714
            t6 = inject_bool(t715)
        else:
            t716 = project_int(t702)
            t717 = project_big(t704)
            t718 = t716 != t717
            t6 = inject_bool(t718)
else:
    t719 = is_bool(t702)
    if t719:
        t720 = is_int(t704)
        if t720:
            t721 = project_bool(t702)
            t722 = project_int(t704)
            t723 = t721 != t722
            t6 = inject_bool(t723)
        else:
            t724 = is_bool(t704)
            if t724:
                t725 = project_bool(t702)
                t726 = project_bool(t704)
                t727 = t725 != t726
                t6 = inject_bool(t727)
            else:
                t728 = project_bool(t702)
                t729 = project_big(t704)
                t730 = t728 != t729
                t6 = inject_bool(t730)
    else:
        t731 = is_int(t704)
        if t731:
            t732 = project_big(t702)
            t733 = project_int(t704)
            t734 = t732 != t733
            t6 = inject_bool(t734)
        else:
            t735 = is_bool(t704)
            if t735:
                t736 = project_big(t702)
                t737 = project_bool(t704)
                t738 = t736 != t737
                t6 = inject_bool(t738)
            else:
                t739 = project_big(t702)
                t740 = project_big(t704)
                t741 = not_equal(t739, t740)
                t6 = inject_bool(t741)