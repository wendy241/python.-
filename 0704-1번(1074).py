def recur(a, b, size):
    global cnt

    if a > r or a + size <= r or b > c or b + size <= c:
        cnt += size * size
        return

    if size == 1:
        if a == r and b == c:
            print(cnt)
            exit()
        cnt += 1
        return

    recur(a, b, size//2)
    recur(a, b + size//2, size//2)
    recur(a + size//2, b, size//2)
    recur(a + size//2, b + size//2, size//2)

n, r, c = map(int, input().split())
cnt = 0
recur(0, 0, 2**n)