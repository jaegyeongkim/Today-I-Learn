arr = [1, 2, 3, 4, 5]
N = len(arr)
selected = [0] * N

def powerset(idx):
    if idx == N:
        for i in range(N):
            if selected[i] == 1:
                print(arr[i], end=' ')
        print()
        return
    selected[idx] = 1
    powerset(idx+1)
    selected[idx] = 0
    powerset(idx+1)
powerset(0)