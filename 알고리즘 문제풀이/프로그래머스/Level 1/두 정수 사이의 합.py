def solution(a, b):
    answer = 0
    if a > b:
        for num in range(b, a+1):
            answer += num
    elif a < b:
        for num in range(a, b+1):
            answer += num
    elif a == b:
        answer = a

    return answer


# 두번째 방법
# for문을 쓰는 거 보다 sum 쓰는 게 훨씬 빠름
def solution(a, b):
    answer = 0
    if a > b:
        answer = sum(range(b, a+1))
    elif a < b:
        answer = sum(range(a, b+1))
    elif a == b:
        answer = a
    return answer
