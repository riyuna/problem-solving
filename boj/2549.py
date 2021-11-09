L=[]
for i in ' '*4:L.append(list(map(int,input().split())))
ans=8

def col_rt(n):
    rem=L[3][n]
    for i in range(3):
        L[3-i][n]=L[2-i][n]
    L[0][n]=rem

def row_rt(n):
    rem=L[n][3]
    for i in range(3):
        L[n][3-i]=L[n][2-i]
    L[n][0]=rem

res=[[0,0,0] for i in range(10)]

def solve(ct, row, col):
    global ans
    diff=0
    for i in range(16):
        if L[i//4][i%4]!=i+1:diff+=1
    
    if ans<=ct+(diff+3)//4:
        return False

    if diff==0:
        ans=ct
        return True
    
    state=False

    for i in range(row, 4):
        for j in range(3):
            row_rt(i)
            if solve(ct+1, i+1, 0):
                res[ct]=['row',i+1,j+1]
                state=True
        row_rt(i)
    
    for i in range(col, 4):
        for j in range(3):
            col_rt(i)
            if solve(ct+1, 0, i+1):
                res[ct]=['col', i+1, j+1]
                state=True
        col_rt(i)
    
    return state

solve(0,0,0)
print(ans)
for i in range(ans):
    a,b,c=res[i]
    if a=='col':print(2, b, c)
    else:print(1, b, c)