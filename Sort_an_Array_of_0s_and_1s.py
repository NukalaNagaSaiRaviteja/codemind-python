n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in range(n):
    if l[i]==0:
        l1.append(l[i])
    else:
        l2.append(l[i])
l3=l1+l2
print(*l3)
