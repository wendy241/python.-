def recur(n):
    if n==1:
        arr.append(1)
        return
    if n%2==0:
        arr.append(0)
    elif n%2==1:
        arr.append(1)
    return recur(n//2)

arr=[]

n=int(input())
recur(n)
arr[:]=arr[::-1]
for i in range(len(arr)):
    print(arr[i], end='')