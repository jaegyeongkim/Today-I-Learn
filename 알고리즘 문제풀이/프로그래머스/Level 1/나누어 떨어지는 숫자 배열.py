def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer
