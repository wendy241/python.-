a, b = map(int, input().split())
arr = [0 for i in range(b)]
test = [0 for i in range(a)]
visited = [False for i in range(a)]

k = input().split()

for i in range(len(test)):
    test[i] = int(k[i])

test.sort()

#a : 숫자 개수(진수 역할)/ b : 자리 수
#arr : 수열 만들어줄 리스트/ test : a에서 입력받은 개수만큼의 숫자 리스트
def recur(cur):
    if cur == b:
        for j in range(len(arr)):
            print(arr[j], end=' ')
        print()
        return

    for i in range(a):
        if visited[i]:
            continue

        arr[cur] = test[i]
        visited[i] = True
        recur(cur + 1)
        visited[i] = False

recur(0)