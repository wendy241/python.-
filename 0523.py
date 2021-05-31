# ##1번(런타d임)
ball=[1, 0, 0]
k=['A', 'B', 'C']
n=input()

for i in range(len(n)):
    ex=0
    if n[i]==k[2]:
        ex=ball[0]
        ball[0]=ball[-1]
        ball[-1]=ex
    else:
        ex=ball[i]
        ball[i]=ball[i+1]
        ball[i+1]=ex

for i in range(len(ball)):
    if ball[i]==1:
        print(i+1)

##2번

# ##3번(시간제한) O(1000000+n)이라 생각함.
# n=int(input())
# lst=[0]*1000000
# for i in range(n):
#     k=int(input())
#     lst[k]+=1
#
# for i in range(1000000):
#     if lst[i]>0:
#         for k in range(lst[i]):
# #             print(i)
#
##4번
lst=[0]*500000;n=0
j=[]
num=int(input())
for _ in range(num):
    k=int(input())
    n+=k
    lst[k]+=1
print(n/num)#
for i in range(num):

        j.append(i)
if len(max(j))>=2:
    print()
print(j[-1]-j[0])

# ##5번
# n=input().split()
# rp=[1, 1, 2, 2, 2, 8]
# result=[]
# for i in range(len(n)):
#     n[i]=int(n[i])
#
# for i in range(len(rp)):
#     if n[i]==rp[i]:
#         result.append(0)
#     else:
#         result.append(rp[i]-n[i])
# for i in range(len(result)):
#     print(result[i], end=' ')

# ##6번
#
# n=input()
# while n!='0':
#     width = 0
#     for i in range(len(n)):
#         if n[i]=='1':
#             width+=2
#         elif n[i]=='0':
#             width+=4
#         else:
#             width+=3
#     width+=2;width+=len(n)-1
#     print(width)
#     n=input()

# ##7번
# n=int(input())
# n%=8
#
# if n==1:
#     print(1)
# elif n==2 or n==0:
#     print(2)
# elif n==3 or n==7:
#     print(3)
# elif n==4 or n==6:
#     print(4)
# elif n==5:
#     print(5)

# ##8번 -딕셔너리
# a='-''\\''(@?>&%'
# dict1={}
# for i in range(len(a)):
#     dict1[a[i]]=i
# dict1['/']=-1
# ans=0
# m=1
# n=input()
# while n!='#':
#     for i in n[::-1]:
#         ans+=dict1[i]*m
#         m*=8
#     print(ans)
#     ans=0;m=1
#     n=input()

# ##9번 윷놀이
# result=["E", "A", "B", "C", "D"]
# for i in range(3):
#     cnt=0
#     n=input().split()
#     for i in range(len(n)):
#         if n[i]=='1':
#             cnt+=1
#     for k in range(len(result)):
#         if cnt==4-k:
#             print(result[k])

# ##10번 모음의 개수
#
# while True:
#     n = input()
#     text = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     cnt=0
#     if n=='#':
#         break
#     for i in range(len(n)):
#         if n[i] in text:
#             cnt+=1
#     print(cnt)

##11번 문자메세지
##12번 팬케이크 사랑
# ##13번 유학 금지 #런타임에러ㅠㅅㅠ
# n=input()
# prohibit='CAMBRIDGE'
# for i in range(len(n)):
#     if n[i] in prohibit:
#         n=n.replace(n[i], '')
#print(n)

# ##14번 2009년
# import datetime
# n=input().split()
# for _ in range(len(n)):
#     n[_]=int(n[_])
# weekday=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# y=2009;m=int(n[-1]);d=int(n[0])
# ans=weekday[datetime.date(y, m, n).weekday()]
# print(ans)

# ##15번 찍기
# n=int(input())
# test=input()
# id='Adrian','Bruno','Goran'
# ans='ABC','BABC','CCAABB'
# ID={}
# g=[]
# cnt=0
# for i in range(3):
#     ID[id[i]]=ans[i]
# for _ in range(test):
#     if test[_]==ans[_]:
#         cnt+=1
# g.append(cnt)
#
# ##16번 알람시계
# n=input().split(":")
# for _ in range(len(n)):
#     n[_]=int(n[_])
# n[0]%=24
# n[-1]%=60
# for _ in range(len(n)):
#     if n[_]==n[-1]:
#         print(n[_])
#     else:
#         print(n[_], end=':')


# # ##17번 중간계 전쟁
# g=[1, 2, 3, 3, 4, 10]
# s=[1, 2, 2, 2, 3, 5, 10]
# result=['Good triumphs over Evil', 'Evil eradicates all trace of Good', 'No victor on this battle field']
# T=int(input())
# for i in range(T):
#     g_result, s_result=0, 0
#     g_input=input().split()
#     s_input=input().split()
#     for _ in range(len(g_input)):
#         g_input[_]=int(g_input[_])
#         g_result+=g_input[_]*g[_]
#     for _ in range(len(s_input)):
#         s_input[_]=int(s_input[_])
#         s_result+=s_input[_]*s[_]
#     if g_result>s_result:
#         print("Battle %d: %s"%(i+1, result[0]))
#     elif g_result<s_result:
#         print("Battle %d: %s" % (i + 1, result[1]))
#     else:
#         print("Battle %d: %s" % (i + 1, result[2]))

##18번 The Seven Percent Soultion
# ##19번 거스름돈
# n=int(input())
# l=[500, 100, 50, 10, 5, 1]
# k=1000-n
# cnt=0
# for _ in range(len(l)):
#     while k//l[_]!=0:
#         k-=l[_]
#         cnt+=1
# print(cnt)

# ##20번 다이얼
# a='ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'
# num=[3, 4, 5, 6, 7, 8, 9, 10]
# n=input()
# t=0
# for _ in range(len(n)):
#     for i in range(len(a)):
#         if n[_] in a[i]:
#             t+=num[i]
# print(t)

##21번 P,MTHBGWB
##22번 Rotating letters
##23번 Icon Scalling
##24번 Tawla
##25번 STROJOPIS