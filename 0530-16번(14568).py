n=int(input())
cnt=0

for i in range(1, n+1):
    for j in range(1, n+1):
        if i%2==0:
            A, B = i, j
            C=n-A-B
            if A>0 and B>0 and C>0:
                if C>=B+2:
                    cnt+=1
print(cnt)