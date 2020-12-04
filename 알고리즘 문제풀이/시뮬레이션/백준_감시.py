import sys
sys.stdin = open('백준_감시.txt')

T = int(input())
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] # 상 우 하 좌
# direction : 방향
# arr: 카메라 번호 , 위치

def coloring(selected, ni, nj, d):
    while 1:
        ni += di[d]
        nj += dj[d]
        if ni < 0 or ni >= N:
            break
        if nj < 0 or nj >= M:
            break
        if arr[ni][nj] == 6:
            break
        selected[ni][nj] = 1
    return selected

def check_square_area(direction):
    global min_cnt
    selected = [[0] * M for _ in range(N)]
    for i in range(len(walls)):
        selected[walls[i][0]][walls[i][1]] = 6
    for i in range(len(direction)):
        ni, nj = cctvs[i][1], cctvs[i][2]
        selected[ni][nj] = 1
        if cctvs[i][0] == 1:
            d = direction[i]
            selected = coloring(selected, ni, nj, d)

        elif cctvs[i][0] == 2:
            if direction[i] == 0 or direction[i] == 2:
                for d in range(0, 3, 2):
                    selected = coloring(selected, ni, nj, d)
            elif direction[i] == 1 or direction[i] == 3:
                    
                for d in range(1, 4, 2):
                    selected = coloring(selected, ni, nj, d)
        elif cctvs[i][0] == 3:
            if direction[i] == 0:
                for d in range(2):
                    selected = coloring(selected, ni, nj, d)
            elif direction[i] == 1:
                for d in range(1, 3):
                    selected = coloring(selected, ni, nj, d)
            elif direction[i] == 2:
                for d in range(2, 4):
                    selected = coloring(selected, ni, nj, d)
            elif direction[i] == 3:
                for d in range(0, 4, 3):
                    selected = coloring(selected, ni, nj, d)
        elif cctvs[i][0] == 4:
            if direction[i] == 0:
                for d in range(4):
                    if d == 2:
                        continue
                    selected = coloring(selected, ni, nj, d)
            elif direction[i] == 1:
                for d in range(4):
                    if d == 3:
                        continue
                    selected = coloring(selected, ni, nj, d)
            elif direction[i] == 2:
                for d in range(4):
                    if d == 0:
                        continue
                    selected = coloring(selected, ni, nj, d)
            elif direction[i] == 3:
                for d in range(4):
                    if d == 1:
                        continue
                    selected = coloring(selected, ni, nj, d)
        elif cctvs[i][0] == 5:
            for d in range(4):
                selected = coloring(selected, ni, nj, d)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if selected[i][j] == 0:
                cnt += 1
    if min_cnt > cnt:
        min_cnt = cnt
    return

def permutaion(idx, direction):
    global min_cnt
    if min_cnt == 0:
        return
    if idx == len(direction):
        check_square_area(direction)
        return
    for i in range(4):
        if direction[idx] == 5:
            permutaion(idx+1, direction)
            break
        direction[idx] = i
        permutaion(idx+1, direction)
        

N, M = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(N))
cctvs = []
walls = []
min_cnt = N*M
for n in range(N):
    for m in range(M):
        if 1 <= arr[n][m] <= 5:
            cctvs.append([arr[n][m], n, m])
        elif arr[n][m] == 6:
            walls.append([n, m])

direction = [0] * len(cctvs)
for i in range(len(cctvs)):
    if cctvs[i][0] == 5:
        direction[i] = 5
permutaion(0, direction)
print(min_cnt)