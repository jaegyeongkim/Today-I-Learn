def solution(n):
    numbers = [0] *(n+1)
    cnt = 0
    for i in range(2, n+1):
        if numbers[i] == 0:
            cnt += 1
            ratio = 2
            while i*ratio < n+1:
                numbers[i*ratio] = 1
                ratio += 1
    return cnt