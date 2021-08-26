import numpy as np


class NormBase:
    """Base class of normalizations.
    """
    def __init__(self, num_channels, gamma=None, beta=None, eps=1e-5):
        """Initialization.
        `gamma` and `beta` are learnable parameters which are denoted as
        `gamma` and `beta` in the equation.
        """
        self.C = num_channels
        self.eps = eps

        self.gamma = gamma if gamma is not None else np.random.uniform(size=self.C)
        self.beta = beta if beta is not None else np.random.uniform(size=self.C)

    def forward(self, input):
        raise NotImplementedError


class InstanceNorm(NormBase):
    def forward(self, input):
        """Please write your code!
        The shape of returned numpy array should have a same shape with input array.
        """
        N=len(input)
        C=len(input[0])
        H=len(input[0][0])
        w=len(input[0][0][0][0])
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
                siglist[i][j]+=self.eps
                siglist[i][j]**=0.5
        
        for i in range(N):
            for j in range(C):
                for k in range(H):
                    for s in range(w):
                        xi=(input[i][j][k][s]-meanlist[i][j])/siglist[i][j]
                        res[i][j][k][s] = self.gamma*xi+self.beta
        return res