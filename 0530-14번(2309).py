a=[]
for _ in range(9):
    a.append(int(input()))
for _ in range(len(a)):
    for i in range(len(a)):
        if a[_]+a[i]==sum(a)-100:
            if a[_]==a[i]:
                continue
            else:
                a[_], a[i]=-1, -1
                a.sort()
                for l in range(len(a)):
                    if a[l]>=0:
                        print(a[l])