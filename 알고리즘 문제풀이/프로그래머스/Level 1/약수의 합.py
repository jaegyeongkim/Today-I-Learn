def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    answer = 1 + n
    for i in range(2, n//2+1):
        if n%i == 0:
            answer += i
    return answers