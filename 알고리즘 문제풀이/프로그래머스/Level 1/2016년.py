def calculation(date):
    if date % 7 == 0:
        return "THU"
    elif date % 7 == 1:
        return "FRI"
    elif date % 7 == 2:
        return "SAT"
    elif date % 7 == 3:
        return "SUN"
    elif date % 7 == 4:
        return "MON"
    elif date % 7 == 5:
        return "TUE"
    elif date % 7 == 6:
        return "WED"


def solution(a, b):

    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_sum = [0] * 13
    for i in range(1, len(month)):
        month_sum[i] = month_sum[i-1] + month[i]

    answer = calculation(month_sum[a-1] + b)
    return answer
