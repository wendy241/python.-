m, n = map(int, input().split())
arr = [0 for i in range(n)]

def recur(cur, start):
    if cur == n:
        for i in range(len(arr)):
            print(arr[i], end=' ')
        return

    for i in range(start, m):
        arr[cur] = i + 1
        recur(cur + 1, i)

recur(0, 0)