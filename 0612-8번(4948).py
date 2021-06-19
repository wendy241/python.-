n = int(input())
while n != 0:
    prime = [True] * (2*n+1)
    cnt=0
    for i in range(2, 2*n+1):
        if i * i > 2*n:
            break
        if not prime[i]:
            continue

        for j in range(i*i, 2*n+1, i):
            if prime[j]:
                prime[j]=False
    for i in range(n+1, 2*n+1):
        if prime[i]:
            cnt+=1
    print(cnt)
    n = int(input())