def solution(n):
    arr = [[0] * n for _ in range(n)]
    total = n*(n+1)//2
    i, j = 0, 0
    cnt = 1
    di = [1, 0, -1]
    dj = [0, 1, -1]
    d = 0
    while cnt < total+1:
        arr[i][j] = cnt
        cnt += 1
        
        i += di[d]
        j += dj[d]
        if i < 0 or i >= n or j < 0 or j >= n or arr[i][j] != 0:
            i -= di[d]
            j -= dj[d]
            d += 1
            if d >= 3:
                d = d%3
            i += di[d]
            j += dj[d]
            
    answer = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                answer.append(arr[i][j])
    return answer