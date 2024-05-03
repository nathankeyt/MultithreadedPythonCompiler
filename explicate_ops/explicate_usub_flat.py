t1035 = t32
t1038 = is_int(t1035)
if t1038:
    t1039 = project_int(t1035)
    t1040 = -t1039
    t33 = inject_int(t1040)
else:
    t1041 = is_bool(t1035)
    if t1041:
        t1042 = project_bool(t1035)
        t1043 = -t1042
        t33 = inject_int(t1043)
    else:
        throw_type_error()