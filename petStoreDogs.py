N=int(input())
ways=[0]*(N+1)
for ctr in range(1,N+1):
    if ctr<=2:
        ways[ctr]=ctr
    else:
        passive=(ctr-1)*ways[ctr-2]
        ways[ctr]=passive+ways[ctr-1]
print(ways[N])
