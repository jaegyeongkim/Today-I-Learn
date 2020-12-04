def solution(n):
    result = ''
    answer = 0
    while n != 0:
        rest = str(n % 3)
        n = n // 3
        result += rest

    for i in range(len(result)-1, -1, -1):
        answer += int(result[i])*3**(len(result)-1-i)
    print(answer)

    return answer