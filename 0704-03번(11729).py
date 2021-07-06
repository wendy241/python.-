N = int(input())
ans = 0
for i in range(N):
    ans = 2 * ans + 1

def recur(s, e, p, n):
    if n == 1:
        print(str(s) + ' ' + str(e))
        return
    recur(s, p, e, n - 1)
    recur(s, e, p, 1)
    recur(p, e, s, n - 1)

print(ans)
recur(1, 3, 2, N)