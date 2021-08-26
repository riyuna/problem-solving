n=int(input())
def solve(L):
    if len(L)==1:
        res=[0,0,0]
        res[L[0][0]+1]+=1
        return res

    check_bool=True
    check_same=L[0][0]
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][j]!=check_same:
                check_bool=False
                break
    if check_bool:
        res=[0,0,0]
        res[L[0][0]+1]+=1
        return res
    res=[0,0,0]
    for i in range(9):
        val=-2
        equal=True
        x=i//3
        y=i%3
        m=len(L)//3
        M=[]
        for j in range(m*x,m*(x+1)):
            MM=[]
            for k in range(m*y, m*(y+1)):
                MM.append(L[j][k])
                if val!=-2 and L[j][k]!=val:
                    equal=False
                val=L[j][k]
            M.append(MM)
        if equal:
            res[val+1]+=1
        else:
            rres=solve(M)
            res[0]+=rres[0]
            res[1]+=rres[1]
            res[2]+=rres[2]
    return res
L=[]
for i in ' '*n:L.append(list(map(int,input().split())))

for i in solve(L):print(i)