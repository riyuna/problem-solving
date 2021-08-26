import numpy as np

N=2
C=2
H=1
w=1
eps = 10**-5
gamma = 1
beta = 0
input= [
    [[[1]],[[2]]],
    [[[3]],[[4]]]
]
res = np.zeros((N,C,H,w))
meanlist = [[0]*C for i in range(N)]

for i in range(N):
    for j in range(C):
        for k in range(H):
            for s in range(w):
                meanlist[i][j]+=input[i][j][k][s]
        meanlist[i][j]/=(H*w)

siglist = [[0]*C for i in range(N)]

for i in range(N):
    for j in range(C):
        for k in range(H):
            for s in range(w):
                siglist[i][j]+=(input[i][j][k][s]-meanlist[i][j])**2
        siglist[i][j]/=(H*w)
        siglist[i][j]+=eps
        siglist[i][j]**=0.5

for i in range(N):
    for j in range(C):
        for k in range(H):
            for s in range(w):
                xi=(input[i][j][k][s]-meanlist[i][j])/siglist[i][j]
                res[i][j][k][s] = gamma*xi+beta
                
print(res)