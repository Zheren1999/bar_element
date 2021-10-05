import numpy as np
import matplotlib.pyplot as plt
import math
import bisect
from scipy.interpolate import interp1d


mcr=2
k1=16*(math.pi)**4

k3=0.1*k1
s=2*k3/(k1+(math.pi)**4*mcr**4)



def KroneckerDelta (j,k):
    d=0
    if j==k:
        d=1;
    else:
        d=0
    return d


def Im(m):
    e=[]
    N=5
    for p in range(1,N):
        for q in range (1,N):
            for r in range (1,N):
                 e.append(KroneckerDelta(p+q,r+m)-
                         KroneckerDelta(abs(p-q),r+m)-
                         KroneckerDelta(p+q,abs(r-m))+
                         KroneckerDelta(abs(p-q),abs(r-m))+
                         KroneckerDelta(p,q)*KroneckerDelta(r,m))
                 r=sum(e)
    return(r)

def am(m):
    return ( ( (m**2*(math.pi)**2+k1/(m**2*(math.pi)**2) ))/ (((math.pi)**2*mcr**2)+k1/((math.pi)**2*mcr**2)) )


x_start = 0
x_stop = 1
x1_start = 0
x1_stop = 1
L = 5
x = np.linspace(x_start, x_stop, L+1)
x1= np.linspace(x1_start, x1_stop, L+1)
#x1= [0.2,0.2,0.2,0.2,0.2,0.2]
#x= [0,0.2,0.4,0.6,0.8,1]
print (x1)
#print (x2)
y=[1,1,1,1,1,1]  
def f(x):
    return ((x[m+1]+x1[m+1])*(am(m)*x[m]-s*mcr**2*Im(m)/(8*m**2))-(x[m]+x1[m])*(am(m+1)*x[m+1]-s*mcr**2*Im(m+1)/(8*(m+1)**2)))

def df(x):

   return ((((x[m+2]+x1[m+2])*(am(m+1)*x[m+1]-s*mcr**2*Im(m+1)/(8*(m+1)**2))-
             (x[m+1]+x1[m+1])*(am(m+2)*x[m+2]-s*mcr**2*Im(m+2)/(8*(m+2)**2)) )-
            ((x[m+1]+x1[m+1])*(am(m)*x[m]-s*mcr**2*Im(m)/(8*m**2))-
            (x[m]+x1[m])*(am(m+1)*x[m+1]-s*mcr**2*Im(m+1)/(8*(m+1)**2))))/(x[m+1]-x[m]))



for m in range (1, L-1):
    while abs(f(x))>1e-6:
        print ('x',x[m])
        print ('f',f(x))
        x[m]=x[m]-f(x)/df(x)
        
    print ('for m=1...L, x[m]',x[m])
a=[]
for m in range (1,L):
    a.append((am(m)*x[m]-s*mcr**2*Im(m)/(8*m**2))/(x[m]+x1[m]))

#a.append(0)
#a.append(0)
x = np.delete(x, 4)
x = np.delete(x, 4) 
print (a)
print (x)



U= []
'''
def interpolation(aval):
    w = bisect.bisect_left(t, aval)
    z = t[w-1]
    s = t[w]
    if z==s: return tee[x]
    delta = float(aval-z)/(s-z)
    return delta*tee[s] + (1-delta)*tee[z]

dictionary = dict(zip(x, a))
t = sorted(dictionary)
tee = dictionary
interpolation = np.vectorize(interpolation) 
vv = np.linspace(0, 1, 500)

U=np.append(U,interpolation(vv))
'''

#print ('U',U)
#print ('vv',vv)
#plt.plot(vv,U,'black', label='load')
plt.plot(x, a)
#f = interp1d(x, a)
#xnew = np.linspace(0, 1, num=54)

#plt.plot(xnew, f(xnew))

plt.xlabel('x', fontsize=10,  color='black')
plt.ylabel('y(x)', fontsize=10,  color='black')
plt.grid()
plt.legend()
plt.show()
