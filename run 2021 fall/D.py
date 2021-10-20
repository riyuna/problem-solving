from copy import deepcopy
def rotate(L,i,j,n):
    res=deepcopy(L)
    for ii in range(n):
        for jj in range(n):
            res[i+ii][j+jj]=[]