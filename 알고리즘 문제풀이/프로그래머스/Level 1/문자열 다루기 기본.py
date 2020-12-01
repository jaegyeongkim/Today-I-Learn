def solution(s):
    if len(s) == 4 or len(s) == 6:
        for word in s:
            if ord(word) < 48 or ord(word) > 58:
                return False
    else:
        return False
    return True


# def solution(s):
#     if len(s) == 4 or len(s) == 6:
#         if s.isdigit():
#             return True
#     return False
