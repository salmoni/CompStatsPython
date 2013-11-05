def GetGroups(groupingvars):
    groups = []
    k = len(groupingvars)
    N = len(groupingvars[0])
    for idx in range(N):
        row = [var[idx] for var in groupingvars]
        if row not in groups:
            groups.append(row)
    return groups

def ExtractGroupsData(group, groupingvars, variable):
    N = len(variable)
    data = []
    for idx in range(N):
        row = [element[idx] for element in groupingvars]
        if group == row:
            data.append(variable[idx])
    return data

