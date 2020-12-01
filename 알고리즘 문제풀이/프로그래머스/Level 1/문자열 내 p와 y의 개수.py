def solution(s):
    answer = True
    p_cnt = 0
    y_cnt = 0
    for word in s:
        if word == 'p' or word == 'P':
            p_cnt += 1
        elif word == 'y' or word == 'Y':
            y_cnt += 1
    if p_cnt != y_cnt:
        return False
    return True
