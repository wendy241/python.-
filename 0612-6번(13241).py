a, b=map(int, input().split())

ta, tb = a, b

while ta % tb !=0:
    temp = ta % tb
    ta = tb
    tb = temp

print(a*b//tb)