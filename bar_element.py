import numpy as np
from scipy.linalg import eigh

p=1
A=1
E=1
L=1
def bar_element(n):
    
    m=np.array([[2,1],
                [1,2]])/(6*n*p*A*L)
    k=np.array([[1,-1],
                [-1,1]])*(n*E*A/L)

    s=(n+1,n+1)
    M=np.zeros(s)
    K=np.zeros(s)
    
    for i in range (0,n):
        M1=np.zeros(s)
        K1=np.zeros(s)
        M1[i:i+2, i:i+2]=m
        K1[i:i+2, i:i+2]=k
        M=M+M1
        K=K+K1
    
    w,b=eigh(K,M)
    return M, K, w

M,K,w=bar_element(2)

print(M)
print(K)
print(np.sqrt(w))

