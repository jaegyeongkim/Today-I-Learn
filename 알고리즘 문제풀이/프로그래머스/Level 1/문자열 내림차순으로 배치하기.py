def solution(s):
    s_dic = {}
    for i in s:
        if i in s_dic.keys():
            s_dic[i][1] += 1
        else:
            s_dic[i] = [ord(i), 1]
    result = sorted(s_dic.items(), key=lambda x: -x[1][0])
    answer = ''
    back = ''
    for word, weight in result:
        answer += word*weight[1]
    return answer


def solution(s):
    answer = ''
    answer = answer.join(sorted(s, reverse=True))
    return answer
