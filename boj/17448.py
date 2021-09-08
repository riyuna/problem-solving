from fractions import Fraction
n,k=map(int,input().split())
L=list(map(int,input().split()))
L=sorted(L, key=abs)
print(L)
m=10**9+7
def solve(L, k):
    pt=0
    for i in L:
        if i==0:pt+=1
    L=L[pt:]
    if len(L)==0:return 1
    if len(L)<k:
        res=1
        for i in L:
            res*=abs(i)
            res%=m
        return res
    for i in range(len(L)):L[i]=-L[i]
    res = 1
    frontL=L[:len(L)-k]
    backL=L[len(L)-k:]
    for i in backL:
        if i<0:res*=-1
    ans=1
    for i in range(k):
        ans*=abs(backL[i])
        ans%=m
    if res==1:
        return ans
    ans_list = []
    ans1=abs(backL[0])
    ans_list.append(Fraction(1, ans1))
    min_pos = -1
    max_pos=-1
    min_neg=-1
    max_neg=-1
    for i in range(k):
        if backL[i]>0 and min_pos==-1:min_pos=i
        if backL[i]<0 and min_neg==-1:min_neg=i
    for i in range(len(frontL)):
        if frontL[i]>0:max_pos=i
        if frontL[i]<0:max_neg=i
    
    ans2=1
    ans3=1
    if min_pos!=-1 and max_neg!=-1:
        ans2=Fraction(abs(frontL[max_neg]), abs(backL[min_pos]))
        ans_list.append(ans2)

    if max_pos!=-1 and min_neg!=-1:
        ans3=Fraction(abs(frontL[max_pos]), abs(backL[min_neg]))
        ans_list.append(ans3)
    
    ans_res=max(ans_list)
    num = ans_res.numerator
    den = ans_res.denominator
    ans*=num
    ans%=m
    ans*=pow(den, m-2, m)
    ans%=m
    return ans
print(solve(L,k))