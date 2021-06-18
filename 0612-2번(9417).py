M=int(input())

for _ in range(M):
    k=input().split()

    for l in range(len(k)):
        k[l]=int(k[l])

    arr=[]

    for i in range(len(k)):
        for j in range(len(k)):

            if i==j:
                continue

            if k[i] < k[j]:
                a=k[j]
                b=k[i]
            else:
                a=k[i];b=k[j]

            while a % b != 0:
                temp = a % b
                a = b
                b = temp

            arr.append(b)
    print(max(arr))
