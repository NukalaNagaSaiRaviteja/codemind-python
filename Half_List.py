a=int(input())
l=list(map(int,input().split()))
m=a//2-1
n=a//2
for i in l:
    r=l[:m:-1]
    p=l[:n:]
    s=r+p
print(*s)