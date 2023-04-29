l=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
n=[]
for i in m:
    if a>i or b<i:
        n.append(i)
if len(n)>0:
    print(max(n))
else:
    print(-1)