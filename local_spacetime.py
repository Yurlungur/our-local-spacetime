#!/usr/bin/env python

# Author: Jonah Miller (jonah.maxwell.miller@gmail.com)
# Time-stamp: <2015-09-06 16:45:52 (jmiller)>

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

f_max = 1.2
f_min = -f_max
r_earth = 0.4
r_max = 1.44
N = 100

f = np.linspace(f_min,f_max,N)
s = np.linspace(r_earth,r_max,N)

F,S = np.meshgrid(f,s)

def X1(s,f):
    return s*np.cosh(f)

def T1(s,f):
    return s*np.sinh(f)

def integrand(q):
    return np.sqrt(((1-q)**(-4)-1)/q)

def Y1(s,f):
    upper_bound = 0.25*s*s
    return integrate.quad(integrand,0,upper_bound)[0]

X = X1(S,F)
T = T1(S,F)
Y = np.empty_like(X)
for i in range(Y.shape[0]):
    for j in range(Y.shape[1]):
        Y[i,j] = Y1(S[i,j],F[i,j])

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X,Y,T,rstride=2,cstride=2,
                       cmap=cm.coolwarm,linewidth=1,
                       antialiased=False)
ax.set_zlim3d=(-2,2)
ax.w_zaxis.set_major_locator(LinearLocator(6))

plt.show()

