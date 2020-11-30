def solution(n, lost, reserve):
    answer = 0
    members = [1] * (n+2)
    members[0] = 0
    members[-1] = 0
    for l in lost:
        members[l] = 0

    reserve_members = [0] * (n+2)
    for r in reserve:
        reserve_members[r] = 1

    for i in range(1, len(members)-1):
        if members[i] == 0:
            if reserve_members[i] == 1:
                reserve_members[i] = 0
                members[i] = 1
            elif reserve_members[i-1] == 1:
                if members[i-1] == 0:
                    continue
                reserve_members[i-1] = 0
                members[i] = 1
            elif reserve_members[i+1] == 1:
                if members[i+1] == 0:
                    continue
                reserve_members[i+1] = 0
                members[i] = 1

    answer = sum(members)
    return answer
