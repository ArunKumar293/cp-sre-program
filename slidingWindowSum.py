N,K=map(int,input().split())
arr=list(map(int,input().split()))
maxSum=sum(arr[:K])
for index in range(1,N-K+1):
    currSum=sum(arr[index:index+K])
    if currSum>maxSum:
        maxSum=currSum
print(maxSum)
