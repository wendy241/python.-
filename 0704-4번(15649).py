##4번

a, b = map(int, input().split())
arr = [0 for i in range(b)]
visited = [False for i in range(a)]

def recur(cur):
    if cur == b:
        for j in range(len(arr)):
            print(arr[j], end=' ')
        return

    for i in range(a):
        if visited[i]:
            continue

        arr[cur] = i + 1
        visited[i] = True
        recur(cur + 1)
        visited[i] = False

recur(0)