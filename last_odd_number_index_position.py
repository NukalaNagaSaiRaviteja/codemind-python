n=int(input())
l=list(map(int,input().split()))
o=[]
x=0
for i in range(n):
    if l[i]%2!=0:
        x=i
print(x)
        
    