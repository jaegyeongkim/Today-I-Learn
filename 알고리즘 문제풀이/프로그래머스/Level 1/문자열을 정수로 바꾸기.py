def solution(s):
    answer = 0
    if ord(s[0]) == 45:
        result = s[1:]
        return -int(result)
    else:
        return int(s)
