# def solution(n):
    
#     numbers = [0] * 10
#     while n > 0:
#         rest = n%10
#         n = n//10
#         numbers[rest] += 1
#     answer = ''
#     for i in range(9, -1, -1):
#         for j in range(numbers[i]):
#             answer += str(i)
    
#     return int(answer)

# def solution(n):
    
#     answer = ''  
#     numbers = []
#     while n > 0:
#         rest = n%10
#         n = n//10
#         numbers.append(rest)
#     numbers = sorted(numbers, reverse=True)
#     for i in range(len(numbers)):
#         answer += str(numbers[i])
#     return int(answer)

print(pow(1000, 1/3))