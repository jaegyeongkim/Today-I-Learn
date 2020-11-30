import sys
sys.stdin = open('백준_경사로.txt')


def summation(arr, visited):
    cnt = 0
    for i in range(N):
        for j in range(N-1):
            if arr[i][j]+1 < arr[i][j+1]:
                break
            elif arr[i][j]-1 > arr[i][j+1]:
                break
            elif arr[i][j]+1 == arr[i][j+1]:
                if j-L+1 < 0:
                    break

                is_checked = 0
                for l in range(L):
                    if visited[i][j-l] == 1:
                        is_checked = 1
                        break
                if is_checked:
                    break

                is_same = 1
                for l in range(1, L):
                    if arr[i][j] != arr[i][j-l]:
                        is_same = 0
                        break
                if is_same == 0:
                    break
                for l in range(L):
                    visited[i][j-l] = 1

            elif arr[i][j]-1 == arr[i][j+1]:
                if j+L >= N:
                    break

                is_checked = 0
                for l in range(L):
                    if visited[i][j+1+l] == 1:
                        is_checked = 1
                        break
                if is_checked:
                    break

                is_same = 1
                for l in range(1, L+1):
                    if arr[i][j+1] != arr[i][j+l]:
                        is_same = 0
                        break
                if is_same == 0:
                    break
                for l in range(L):
                    visited[i][j+1+l] = 1
        else:
            # print(i)
            cnt += 1
    return cnt


N, L = map(int, input().split())

arr = list(list(map(int, input().split())) for _ in range(N))
arr_zip = list(zip(*arr))
cnt = 0
checked = [[0]*N for _ in range(N)]

cnt += summation(arr, checked)
checked = [[0]*N for _ in range(N)]
# print()
cnt += summation(arr_zip, checked)
print(cnt)
