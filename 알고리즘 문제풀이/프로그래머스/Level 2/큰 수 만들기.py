def solution(number, k):
    numbers = []
    for i in range(len(number)):
        numbers.append(int(number[i]))
    cnt = 0
    answer = [int(numbers[0])]
    for i in range(1, len(numbers)):
        if answer[-1] < numbers[i]:
            answer.pop(-1)
            answer.append(numbers[i])
            cnt += 1
        else:
            cnt += 1
        if cnt == k:
            break
    answer += numbers[i+1:]
    if len(answer) > len(number)-k:
        answer = answer[:-(len(answer)-len(number)+k)]
    
    result = ''
    for i in range(len(answer)):
        result += str(answer[i])
            
    return result