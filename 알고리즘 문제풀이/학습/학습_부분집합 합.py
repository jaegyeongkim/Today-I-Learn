arr = [1, 2, 3, 4, 5]
N = len(arr)
selected = [0] * N

def powerset(idx, total):
    if idx == N:
        if total == 5:
            for i in range(N):
                if selected[i] == 1:
                    print(arr[i], end=' ')
            print()
        return
    selected[idx] = 1
    total += arr[idx]
    powerset(idx+1, total)
    selected[idx] = 0
    total -= arr[idx]
    powerset(idx+1, total)
powerset(0, 0)