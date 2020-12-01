import sys
sys.stdin = open('백준_톱니바퀴.txt')


tooth_gear = [0]
for _ in range(4):
    tooth_gear.append(input())
K = int(input())
arr = list(list(map(int, input().split())) for _ in range(K))

for i in range(K):
    check = [0] * 5
    check[arr[i][0]] = arr[i][1]
    left = arr[i][0]
    right = arr[i][0]
    while left-1 > 0:
        if tooth_gear[left][6] == tooth_gear[left-1][2]:
            check[left-1] = 0
            break
        else:
            check[left-1] = -check[left]
        left -= 1
    while right+1 < 5:
        if tooth_gear[right][2] == tooth_gear[right+1][6]:
            check[right+1] = 0
            break
        else:
            check[right+1] = -check[right]
        right += 1

    for c in range(1, len(check)):
        if check[c] == 1:
            tooth_gear[c] = tooth_gear[c][-1] + tooth_gear[c][:7]
        elif check[c] == -1:
            tooth_gear[c] = tooth_gear[c][1:] + tooth_gear[c][0]
result = 0
for i in range(1, 5):
    if int(tooth_gear[i][0]) == 1:
        result += 2**(i-1)
print(result)
