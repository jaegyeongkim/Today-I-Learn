def solution(dartResult):
    answer = 0
    i = 0
    answer_list = []
    while i < len(dartResult):
        
        if dartResult[i] == '*':
            answer_list[-1] = answer_list[-1]*2
            if len(answer_list) > 1:
                answer_list[-2] = answer_list[-2]*2
                
        elif dartResult[i] == '#':
            answer_list[-1] = -answer_list[-1]
        else:
            num = dartResult[i]
            while 1:
                if dartResult[i+1] == 'S':
                    answer_list.append(int(num))
                    break
                elif dartResult[i+1] == 'D':
                    answer_list.append(int(num)**2)
                    break
                elif dartResult[i+1] == 'T':
                    answer_list.append(int(num)**3)
                    break
                i += 1
                num += dartResult[i]
            i+=1
        i += 1
    answer = sum(answer_list)
    return answer