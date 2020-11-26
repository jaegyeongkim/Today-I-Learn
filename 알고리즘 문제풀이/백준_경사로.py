import sys
sys.stdin = open('백준_경사로.txt')

def summation(arr, checked):
    cnt = 0
    for i in range(N):
        cnt += 1
        j = 0
        while j < N-1:
            if arr[i][j] + 1 < arr[i][j+1]:
                cnt -= 1
                break
            elif arr[i][j] - 1 > arr[i][j+1]:
                break
            elif arr[i][j]+1 == arr[i][j+1]:
                if j+1-L < 0:
                    cnt -= 1
                    break
                elif arr[i][j] != arr[i][j+1-L]:
                    cnt -= 1
                    break
                else:
                    is_one = 0
                    for l in range(L):
                        if checked[i][j-l] == 1:
                            is_one = 1
                            break
                        checked[i][j-l] = 1
                    if is_one:
                        cnt -= 1
                        break
                    j += L
                    continue
            elif arr[i][j]-1 == arr[i][j+1]:
                if j+L > N-1:
                    cnt -= 1
                    break
                elif arr[i][j+1] != arr[i][j+L]:
                    cnt -= 1
                    break
                else:
                    is_one = 0
                    for l in range(L):
                        if checked[i][j+1+l] == 1:
                            is_one = 1
                            break
                        checked[i][j+1+l] = 1
                    if is_one:
                        cnt -= 1
                        break
                    j += L
                    continue

            j += 1
        print(i, cnt)
    return cnt
T = int(input())

for t in range(1, T+1):
    N, L = map(int, input().split())

    arr = list(list(map(int, input().split())) for _ in range(N))
    arr_zip = list(zip(*arr))
    cnt = 0
    checked = [[0]*N for _ in range(N)]
    cnt += summation(arr, checked)
    cnt += summation(arr_zip, checked)
    print(cnt)


