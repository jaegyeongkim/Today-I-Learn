def solution(progresses, speeds):
    answer = []
    
    while progresses:
        cnt = 0
        is_progress = 0
        for i in range(len(speeds)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
                is_progress = 1
                if progresses[i] >= 100:
                    progresses[i] = 100
        if progresses[0] == 100:
            cnt = 0
            for i in range(len(progresses)):
                if progresses[i] != 100:
                    break
                else:
                    cnt += 1
            answer.append(cnt)
            for _ in range(cnt):
                progresses.pop(0)
                speeds.pop(0)
            
    return answer
    