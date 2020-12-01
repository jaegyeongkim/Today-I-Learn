def solution(strings, n):
    answer = []
    strings_dic = {x: 0 for x in strings}

    for i in range(len(strings)):
        strings_dic[strings[i]] = ord(strings[i][n])
    strings_dic = sorted(strings_dic.items(),
                         key=lambda item: item[1])  # value: [1]

    n = 0
    while n < len(strings):
        key, value = strings_dic[n][0], strings_dic[n][1]
        cnt = 0
        compare = [key]
        for i in range(n+1, len(strings)):
            if strings_dic[i][1] == value:
                cnt += 1
                compare.append(strings_dic[i][0])
            else:
                break

        compare = sorted(compare)
        for com in compare:
            answer.append(com)

        if cnt > 0:
            n += cnt
        n += 1
    return answer
