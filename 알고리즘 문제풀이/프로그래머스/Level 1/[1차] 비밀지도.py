def ox_to_binary(n, number):
    result = ''
    while number:
        rest = number % 2
        number = number // 2
        result += str(rest)
    result = result[::-1]
    while len(result) < n:
        result = '0' + result
    return result
def solution(n, arr1, arr2):
    answer = []
    arr1_list = []
    for i in range(n):
        num1 = ox_to_binary(n, arr1[i])
        num2 = ox_to_binary(n, arr2[i])
        print(num1, num2)
        result = ''
        for j in range(n):
            if num1[j] == '0' and num2[j] == '0':
                result += ' '
            else:
                result += '#'
        answer.append(result)
    return answer