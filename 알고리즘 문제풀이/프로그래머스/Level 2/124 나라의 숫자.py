def solution(n):
    answer = ''
    while n > 0:
        rest = n%3
        n = n//3
        
        if rest == 0:
            n -= 1
            rest = 4
        print(rest)
        answer = str(rest) + answer
    
    return answer
