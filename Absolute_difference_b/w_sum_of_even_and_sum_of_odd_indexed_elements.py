n=int(input())
x=list(map(int,input().split()))
cnt=0
sum=0
for i in range(len(x)):
    if i%2!=0:
        cnt+=x[i]
    else:
        sum+=x[i]
print(abs(sum-cnt))