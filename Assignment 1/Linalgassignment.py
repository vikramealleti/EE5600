import numpy as np
import sympy as sp
from sympy import Eq,solve,symbols

[a1,b1,c1,d1]=[1,1,1,1]
[a2,b2,c2,d2]=[2,3,-1,-4]
a3=0
b3,c3,d3=symbols('b,c,d')
x0=a3
y0,z0=symbols('y,z')
q=np.cross([a1,b1,c1],[a2,b2,c2])

Pp3=Eq(np.dot(q,[a3,b3,c3]),0)

Np3=solve(Pp3,(b3,c3))

b3=Np3[0][0]/Np3[0][0]
c3=Np3[0][1]/Np3[0][0]

Np1=Eq(b1*y0+c1*z0-d1,0)
Np2=Eq(b2*y0+c2*z0-d2,0)

POP=solve((Np1,Np2),(y0,z0))

y0=POP[y0]
z0=POP[z0]

d3=a3*0+ b3*y0 + c3*z0

print('POINT on PLANE (x0,y0,z0) = (',x0,',',y0,',',z0,')')


print('Coefficients of PLANE (a3,b3,c3,d3) = ' '(', a3,',', b3,',', c3,',', d3,')')



