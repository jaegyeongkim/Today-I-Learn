def solution(array, commands):
    answer = []
    for arr in commands:
        i, j, k = arr[0], arr[1], arr[2]
        result = array[i-1:j]
        result.sort()
        answer.append(result[k-1])
    return answer
