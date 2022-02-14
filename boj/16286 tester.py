def solution(w, L):
    # w,n=map(int,input().split())
    # L=list(map(int,input().split()))

    ssum=[0]
    for i in L:ssum.append(ssum[-1]+i)

    def check(x):
        global w
        n=len(L)
        dp=[0]*(n+1)
        dp[0]=1
        dpsum=[0, 1]

        l,r=0,0
        i=0
        while i<n:
            now=ssum[i+1]
            if i:now=ssum[i+1]-ssum[l+1]
            while now>w:
                now=ssum[i+1]-ssum[l+1]
                l+=1
            r=l
            while now>=w-x:
                now=ssum[i+1]-ssum[r+1]
                r+=1
            # print(i,l,r)
            i+=1
            if dpsum[r]>dpsum[l]:dp[i]=1
            else:dp[i]=0
            dpsum.append(dpsum[-1]+dp[i])
        # print(dp)
        # print(dpsum)
        return dp[-1]==1
        
    lo=0
    hi=w
    while lo<hi:
        mid=(lo+hi)//2
        if check(mid):hi=mid
        else:lo=mid+1

    return hi

def brute(w, L):
    m=w
    for i in range(32):
        div=[0]
        if i&1:div.append(0)
        if i&2:div.append(1)
        if i&4:div.append(2)
        if i&8:div.append(3)
        if i&16:div.append(4)
        div.append(5)
        ct=w
        res=True
        for j in range(len(div)-1):
            k=sum(L[div[j]:div[j+1]])
            if k>w:
                res=False
                break
            ct=min(ct, k)
        if res:
            m=min(m, ct)
    return w-m

for i in range(1, 6):
    for j in range(1, 6):
        for k in range(1, 6):
            for l in range(1, 6):
                for m in range(1, 6):
                    L=[i,j,k,l,m]
                    for w in range(max(L), 11):
                        if solution(w,L)!=brute(w,L):
                            print(L, w)
                            print(solution(w, L))
                            print(brute(w,L))