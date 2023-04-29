l=int(input())
m=list(map(int,input().split()))
n=[]
o=[]
for i in m:
    if i%2==0:
        n.append(i)
    else:
        o.append(i)
c=o+n
print(*c)