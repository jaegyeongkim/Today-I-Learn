def solution(N, stages):
    arr = [[0, 0, 0, n] for n in range(N+1)]
    for idx in stages:
        if idx > N:
            for i in range(1, idx):
                arr[i][1] += 1
        else:
            for i in range(1, idx+1):
                arr[i][1] += 1
                if i >= idx:
                    arr[i][0] += 1
    for i in range(1, N+1):
        if arr[i][1] != 0:
            arr[i][2] = arr[i][0] / arr[i][1]
    arr = sorted(arr, key=lambda x:x[2], reverse=True)
    
    answer = []
    for n in range(N+1):
        if arr[n][-1] != 0:
            answer.append(arr[n][-1])
    return answer