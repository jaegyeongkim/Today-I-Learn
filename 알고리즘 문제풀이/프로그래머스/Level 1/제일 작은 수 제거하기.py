def solution(arr):
    answer = []
    arr.pop(arr.index(min(arr)))
    if len(arr) == 0:
        return [-1]
    answer = arr
    
    return answer