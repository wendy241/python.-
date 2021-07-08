a, b = map(int, input().split())
arr = [0 for i in range(b)]
test = [0 for i in range(a)]

k = input().split()

for i in range(len(test)):
    test[i] = int(k[i])

test.sort()

def recur(cur):
    if cur == b:
        for j in range(len(arr)):
            print(arr[j], end=' ')
        print()
        return

    for i in range(0, a):
        arr[cur] = test[i]
        recur(cur + 1)

recur(0)