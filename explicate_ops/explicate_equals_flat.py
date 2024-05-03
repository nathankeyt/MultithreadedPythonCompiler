t839 = t12
t841 = t22
t844 = is_int(t839)
if t844:
    t845 = is_int(t841)
    if t845:
        t846 = project_int(t839)
        t847 = project_int(t841)
        t848 = t846 == t847
        t23 = inject_bool(t848)
    else:
        t849 = is_bool(t841)
        if t849:
            t850 = project_int(t839)
            t851 = project_bool(t841)
            t852 = t850 == t851
            t23 = inject_bool(t852)
        else:
            t853 = project_int(t839)
            t854 = project_big(t841)
            t855 = t853 == t854
            t23 = inject_bool(t855)
else:
    t856 = is_bool(t839)
    if t856:
        t857 = is_int(t841)
        if t857:
            t858 = project_bool(t839)
            t859 = project_int(t841)
            t860 = t858 == t859
            t23 = inject_bool(t860)
        else:
            t861 = is_bool(t841)
            if t861:
                t862 = project_bool(t839)
                t863 = project_bool(t841)
                t864 = t862 == t863
                t23 = inject_bool(t864)
            else:
                t865 = project_bool(t839)
                t866 = project_big(t841)
                t867 = t865 == t866
                t23 = inject_bool(t867)
    else:
        t868 = is_int(t841)
        if t868:
            t869 = project_big(t839)
            t870 = project_int(t841)
            t871 = t869 == t870
            t23 = inject_bool(t871)
        else:
            t872 = is_bool(t841)
            if t872:
                t873 = project_big(t839)
                t874 = project_bool(t841)
                t875 = t873 == t874
                t23 = inject_bool(t875)
            else:
                t876 = project_big(t839)
                t877 = project_big(t841)
                t878 = equal(t876, t877)
                t23 = inject_bool(t878)