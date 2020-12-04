def solution(x):
    result = 0
    origin = x
    while x > 0:
        rest = x%10
        x = x//10
        result += rest
    if origin % result == 0:
        return True
    return False
