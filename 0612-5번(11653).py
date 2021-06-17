N=int(input())

x = N
k=[]
for i in range(2, N+1):
    if i * i > N:
        break
    if x == 1:
        break
    while x % i == 0:
        x//=i
        k.append(i)

if x != 1:
    k.append(x)
k.sort()
for i in range(len(k)):
    print(k[i])