def recur(s, e):
    if s>=e:
        return "true"
    if a[s]==a[e]:
        return recur(s+1, e-1)
    else:
        return "false"

a=input()
print(recur(0, len(a)-1))