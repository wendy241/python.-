a, b, n, w=map(int, input().split())
cnt=0;ans=[]
for i in range(n):
    if a*i + b*(n-i) == w:
        if i==0 or n-i==0:
            continue
        else:
            cnt+=1
            ans=[i, n-i]
if cnt>=2 or cnt==0:
    print(-1)
else:
    for k in range(len(ans)):
        print(ans[k], end=' ')