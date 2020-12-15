import sys
sys.stdin = open('홈 IoT.txt')

def new_arr(Port_connection):
    checked = [0] * len(IoT)
    visited = [[0] * N for _ in range(N)]
    for p in range(len(Port_connection)):
        i, j = Port_connection[p][0], Port_connection[p][1]
        stack = [[i, j, 0]]
        visited[i][j] = 1
        while stack:
            i, j, cnt = stack.pop()
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < N and 0 <= nj < N  and cnt < Rap:
                    stack.append([ni, nj, cnt+1])
                    visited[ni][nj] = 1
    for t in range(len(IoT)):
        i, j = IoT[t][0], IoT[t][1]
        IoT_visited = [[0]*N for _ in range(N)]
        if visited[i][j] == 1:
            checked[t] = 1
            continue
        stack = [[i, j, 0]]
        IoT_visited[i][j] = 1
        while stack:
            i, j, cnt = stack.pop()
            if visited[i][j] == 1:
                checked[t] = 1
                break
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0 <= ni < N and 0 <= nj < N and IoT_visited[ni][nj] == 0 and cnt < IoT[t][2]:
                    IoT_visited[ni][nj] = 1
                    stack.append([ni, nj, cnt+1])
        if checked[t] == 0:
            return -1
    if sum(checked) == len(checked):
        return len(Port_connection)
    else:
        return -1


def combination(idx):
    global min_APconnection, cnt

    if idx == len(Port):
        if 1 <= sum(selected) <= 5 and sum(selected) < min_APconnection:
            cnt += 1
            Port_connection = []
            for i in range(len(Port)):
                if selected[i] == 1:
                    Port_connection.append(Port[i])
            const = new_arr(Port_connection)
            if const == -1:
                return
            if min_APconnection > const:
                min_APconnection = const
        return
    selected[idx] = 0
    combination(idx+1)

    selected[idx] = 1
    combination(idx+1)



T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] # 상 우 하 좌


for t in range(1, T+1):
    N, Rap = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    min_APconnection = 100
    cnt = 0
    Port = []
    IoT = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                Port.append([i, j])
            elif arr[i][j] != 0:
                IoT.append([i, j, arr[i][j]])
    selected = [0] * len(Port)
    combination(0)
    if min_APconnection == 100:
        print('#%d'%t, -1)
    else:
        print('#%d'%t, min_APconnection)
