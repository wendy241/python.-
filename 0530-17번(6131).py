n=int(input())
cnt=0

for A in range(1, 501):
    for B in range(1, 501):
        if n==A**2-B**2:
            cnt+=1
print(cnt)