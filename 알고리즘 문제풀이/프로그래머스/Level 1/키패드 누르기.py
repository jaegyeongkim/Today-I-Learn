def solution(numbers, hand):
    numbers_location = {
        0: (3, 1),
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2)
    }
    answer = ''
    L_location, R_location = (3, 0), (3, 2)
    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            L_location = numbers_location[numbers[i]]
            answer += 'L'
        elif numbers[i] != 0 and numbers[i]%3 == 0:
            R_location = numbers_location[numbers[i]]
            answer += 'R'
        else:
            row, column = numbers_location[numbers[i]][0], numbers_location[numbers[i]][1]
            if abs(row - R_location[0]) + abs(column - R_location[1]) > abs(row - L_location[0]) + abs(column - L_location[1]):
                L_location = numbers_location[numbers[i]]
                answer += 'L'
            elif abs(row - R_location[0]) + abs(column - R_location[1]) < abs(row - L_location[0]) + abs(column - L_location[1]):
                R_location = numbers_location[numbers[i]]
                answer += 'R'
            else:
                if hand == 'left':
                    L_location = numbers_location[numbers[i]]
                    answer += 'L'
                else:
                    R_location = numbers_location[numbers[i]]
                    answer += 'R'
                pass
                
    return answer