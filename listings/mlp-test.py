#!/usr/bin/python

from numpy import *
from matplotlib.pylab import *


w1 = array([-1 ,1, 0])
w2 = array([1, 1, -3])
w3 = array([1,1, -1.5])

act    = lambda x           : 1 if x >= 0 else 0
net    = lambda a     ,    b: sum(a*array(b))
neuron = lambda weight, inpt: act(net(weight,inpt))
mlp    = lambda         inpt: neuron(w3, [ neuron(w1,inpt) , neuron(w2, inpt), 1])

N=100
space = linspace(0,5,N)
M = zeros((N*N,3))

i=0
for x in space:
  for y in space:
    inpt = [x,y,1]
    result = mlp(inpt)
    if result == 1:
      M[i,:] = array((x,y,result))
      i+=1

figure()
hold(True)
scatter(M[:i,0], M[:i,1], 1)
plot(space, space)
plot(space, -space + 3)
savefig('mlp1.png')
show()

