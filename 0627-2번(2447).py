n=int(input())
arr=[[' ' for i in range(6600)] for j in range(6600)]

def recur(x, y, n):
    if n == 1:
        arr[x][y] = '*'
        return

    recur(x, y, n//3)
    recur(x, y + n//3, n//3)
    recur(x, y + 2*n//3, n//3)

    recur(x + n//3, y, n//3)
    recur(x + n//3, y + 2*n//3, n//3)

    recur(x + 2*n//3, y, n//3)
    recur(x + 2*n//3, y + n//3, n//3)
    recur(x + 2*n//3, y + 2*n//3, n//3)

recur(0, 0, n)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print('')