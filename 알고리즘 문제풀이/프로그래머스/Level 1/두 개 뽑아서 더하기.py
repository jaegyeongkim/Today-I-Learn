def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            result = numbers[i] + numbers[j]
            if result not in answer:
                answer.append(result)
    answer.sort()
            
    return answer