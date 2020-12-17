
def solution(n):
    cnt = 0
    num = 0
    while n > num:
        cnt += 1
        num += 3**cnt
        
    answer = ''
    for i in range(cnt-1, -1, -1):
        for j in range(3, 0, -1):
            if n > j*(3**i):
                standard = j*(3**i)
                result = n//standard
                check = 0
                print(n, standard, result)
                for k in range(j, -1, -1):
                    check += 3**k
                print(check)
                if n >= standard + check:
                    result -= 1
                answer += str(result)                      
                n -= result*(3**i)
                break
    print(n, answer)
    
    return answer
