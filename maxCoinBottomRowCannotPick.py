for _ in range(int(input())):
    R,C=map(int,input().split())
    coinMat=[]
    for row in range(R):
        r=[int(element) for element in input().split()]
        coinMat.append(r)
    dpmat=[[0 for col in range(C)]for row in range(R)]
    for col in range(C):
        dpmat[0][col]=coinMat[0][col]
    for row in range(1,R):
        prevRow=dpmat[row-1].copy()
        prevRow.sort()
        firstMax=prevRow[C-1]
        secondMax=prevRow[C-2]
        for col in range(C):
            if dpmat[row-1][col]!=firstMax:
                dpmat[row][col]=coinMat[row][col]+firstMax
            else:
                dpmat[row][col]=coinMat[row][col]+secondMax
    maxCoin=sorted(dpmat[R-1])
    print(maxCoin[C-1])
