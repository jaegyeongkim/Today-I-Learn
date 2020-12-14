import sys
sys.stdin = open('백준_컨베이어 벨트 위의 로봇.txt')

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    arr = []
    for n in range(2*N):
        arr.append([A[n], 0, 0])
    cnt = 0
    cnt_0 = 0
    while 1:
        cnt += 1
        
        # 1칸 회전
        arr = [arr[-1]] + arr[0:-1]
        # 로봇을 내린다.
        arr[N-1][1] = 0
        # 로봇을 전진 시킨다.
        for i in range(N-2, -1, -1):
            if arr[i][1] == 1:
                if arr[i+1][0] > 0 and arr[i+1][1] == 0:
                    arr[i][1] = 0
                    arr[i+1][0] -= 1
                    if arr[i+1][0] == 0 and arr[i+1][2] == 0:
                        arr[i+1][2] = 1
                        cnt_0 += 1

                    if i+1 == N-1:
                        arr[i+1][1] = 0
                    else:
                        arr[i+1][1] = 1
                    
        # 로봇을 올린다.
        if arr[0][0] > 0:    # 내구도가 0보다 크고, 비어있으면
            arr[0][1] = 1   # 채운다.
            arr[0][0] -= 1  # 내구도 1감소
            if arr[0][0] == 0 and arr[0][2] == 0:
                arr[0][2] = 1
                cnt_0 += 1

        # 내구도가 0인 칸의 개수 K면 중지
        if cnt_0 >= K:
            break
    print(cnt)