import sys
sys.stdin = open('알고스탁.txt')
T = int(input())

def differ(i):
    different = []
    for j in range(len(arr)):
        different.append([arr[j][i], arr[j][i + 1] - arr[j][i], 0, j])  # 현재 가격, 다음달과의 차이, 산 거 개수, 인덱스
    different = sorted(different, key=lambda x:x[0])
    return different

for t in range(1, T+1):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    # print(Ms, Ma)
    # for row in arr:
    #     print(row)
    # print()
    origin = Ms
    for i in range(L):
        # print(i)
        # for row in arr:
        #     print(row[i], row[i+1])
        different = differ(i)

        different = sorted(different, key=lambda x:x[1], reverse=True)
        # print(Ms, different)
        if different[0][1] > 0:
            for j in range(len(different)):
                if Ms > different[j][0]:

                    quto = (Ms//different[j][0])
                    Ms -= quto * different[j][0]
                    different[j][2] = (quto)
                elif Ms < different[j][0] < 0:
                    break
        # print(Ms, different)
        for k in range(len(different)):
            if different[k][2] > 0:
                Ms += different[k][2] * arr[different[k][3]][i+1]
        # print(Ms, different)
        # print()
        Ms += Ma
    print('#%d'%t, Ms-origin-Ma*L)