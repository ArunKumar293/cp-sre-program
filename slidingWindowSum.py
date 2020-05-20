N,K=map(int,input().split())
arr=list(map(int,input().split()))
windowSum=sum(arr[:K])
maxSum=windowSum
for index in range(N-K):
    windowSum=windowSum-arr[index]+arr[index+K]
    maxSum=max(maxSum,windowSum)
print(maxSum)
