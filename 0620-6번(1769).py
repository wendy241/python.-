lst=['3', '6', '9']
def recur(a, n):
    if len(n) == 1:

        print(a)
        if n in lst:
            return "YES"
        else:
            return "NO"

    k=0
    for i in range(len(n)):
        k+=int(n[i])
    k=str(k)

    return recur(a+1, k)

n=input()
print(recur(0, n))