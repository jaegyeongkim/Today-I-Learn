def solution(priorities, location):
    new_priorities = []

    for i in range(len(priorities)):
        new_priorities.append([priorities[i], i])
    cnt = 0    
    while new_priorities:
        max_num = max(new_priorities, key=lambda  x:x[0])
        pop_number = new_priorities.pop(0)
        
        if max_num[0] != pop_number[0]:
            new_priorities.append(pop_number)
        else:
            cnt += 1
            if pop_number[1] == location:
                return cnt
        
