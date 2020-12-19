def solution(number, k):
    stack = [number[0]]
    cnt = 0
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and cnt < k:
            cnt += 1
            stack.pop()
        stack.append(num)
    if cnt != k:
        stack = stack[:-(-cnt+k)]
    
    return ''.join(stack)