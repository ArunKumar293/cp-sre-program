import sys
class Link:
    def __init__(self,src,dst,cost):
        self.src=src
        self.dst=dst
        self.cost=cost
N,L=map(int,input().split())
links=[]
for ctr in range(L):
    u,v,c=map(int,input().split())
    l=Link(u,v,c)
    links.append(l)
shortest=[sys.maxsize]*(N+1)
shortest[1]=0
relaxed=True
iteration=1
while iteration<N and relaxed:
    relaxed=False
    for link in links:
        if shortest[link.src]==sys.maxsize:
            continue
        if shortest[link.dst]==sys.maxsize or shortest[link.src]+link.cost<shortest[link.dst]:
            shortest[link.dst]=shortest[link.src]+link.cost
            relaxed=True
    iteration+=1
for city in range(2,N+1):
    print(shortest[city],end=" ")
