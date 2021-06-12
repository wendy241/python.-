lst1=[1, "Yakk", "Doh", "Seh", "Ghar", "Bang", "Sheesh"]
dice=[1, 'Habb Yakk', 'Dobara', 'Dousa', 'Dorgy', "Dabash", 'Dosh']

T=int(input())

for i in range(T):
    k=input().split()
    for l in range(len(k)):
        k[l]=int(k[l])

    a, b=0, 0
    if 5 in k and 6 in k:
        print("Case %d: Sheesh Beesh"%(i+1))
    elif k[0]==k[1]:
        print("Case %d: %s"%(i+1, dice[k[0]]))
    else:
        if k[0]<k[1]:
            a=k[1]
            b=k[0]
        else:
            a=k[0]
            b=k[1]
        print("Case %d: %s"%(i+1, (lst1[a]+' '+lst1[b])))