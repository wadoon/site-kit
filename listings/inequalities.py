#!/usr/bin/python

from numpy import *
from matplotlib.pylab import *

functions = [
    lambda x, y: int(-y + x > 0),
    lambda x, y: int(y + x > 5),
    lambda x, y: int(y**2 + x**2 < 1.5),
    lambda x, y: int(y**2 + x**2 > 3),
]

minx = miny = 0
maxx = maxy = 5
Nx = Ny = 100

xspace = linspace(minx, maxx, Nx)
yspace = linspace(miny, maxy, Ny)


n, m = len(xspace)*len(yspace), 2 + len(functions)
values = zeros((n,m))

i=0
for x in xspace:
    for y in yspace:
        values[i,0] = x
        values[i,1] = y

        for j,fn in enumerate(functions):
            values[i,2+j] = fn(x,y)
        i+=1

print values

figure()
hold(True)

cmap = cm.coolwarm 
print cmap
Nfn = (len(functions))
c = linspace(0.1,0.9,Nfn)
for j in range(Nfn):
    clr = list(cmap(c[j]))
    clr[3] = 0.5
    scatter(values[:,0], values[:,1], 10*values[:, 2+j],
             color = clr,
             edgecolors='none')#, marker='+' )

show()
