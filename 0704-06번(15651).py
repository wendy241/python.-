m, n = map(int, input().split())
arr = [0 for i in range(n)]

def recur(cur): ##cur : arr의 인덱스 번호
    if cur == n:
        for j in range(len(arr)):
            print(arr[j], end=' ')
        return

    for i in range(1, m+1):
        arr[cur] = i
        recur(cur+1)

recur(0)