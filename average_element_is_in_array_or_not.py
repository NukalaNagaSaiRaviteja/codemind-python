n=int(input())
l=list(map(int,input().split()))
s=sum(l)//n
if s not in l:
    print("False")
else:
    print("True")
    