import math
n=int(input())
l=list(map(int,input().split()))
a=max(l)
sum=0
k=0
for i in range(1,a+1):
    k=i*i
    if k in l:
        sum+=k
print(sum)