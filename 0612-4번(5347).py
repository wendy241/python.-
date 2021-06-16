n=int(input())

for i in range(n):
    a, b=map(int, input().split())
    k = a * b

    while a % b != 0:
        temp = a % b
        a = b
        b = temp
    print(k//b)