str1=input().strip()
str2=input().strip()
R=len(str2)
C=len(str1)
mat=[[0 for col in range(C+1)]for row in range(R+1)]
for col in range(C+1):
    mat[0][col]=col
for row in range(1,R+1):
    mat[row][0]=row
for row in range(1,R+1):
    for col in range(1,C+1):
        if str1[col-1]==str2[row-1]:
            mat[row][col]=mat[row-1][col-1]
        else:
            left=mat[row-1][col]
            top=mat[row][col-1]
            topleft=mat[row-1][col-1]
            mat[row][col]=min(topleft,min(top,left))+1
print(mat[R][C])
