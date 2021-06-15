a, b, c, d, e=map(int, input().split())
arr=[a, b, c, d, e]

for i in range(1, 10000000):
    cnt=0
    for j in range(len(arr)):
        if i%arr[j]==0:
            cnt+=1

    if cnt>=3:
        print(i)
        exit()