# -*- coding: utf-8 -*-

# # Berechnung von IsoData (Unsupervised Learning)
# 
# 0. generate data
# 1. guess mu_i 
# 2. classify 
# 3. adapt mu_i
# 4. -> 2



import os,sys 
import numpy as np
from   matplotlib.pylab import *


def newClass( mu, cov, count):
    return np.random.multivariate_normal( mu, cov, count)

X = np.vstack((
 newClass( [ 5, 4] , [[0.5,0.1], [0.3, 0.3] ], 20),
 newClass( [ 6, 3] , [[0.4,0.1], [0.5, 0.3] ], 20),
 newClass( [ 4, 7] , [[0.4,0.1], [0.3, 0.3] ], 20),
# newClass( [ 8, 6] , [[0.4,0.1], [0.6, 0.3] ], 20),
# newClass( [ 5, 1] , [[0.4,0.1], [0.2, 0.3] ], 20), 
# newClass( [ 1, 4] , [[0.3,0.1], [0.3, 0.3] ], 20),
 newClass( [ 1, 1] , [[0.2,0.1], [0.6, 0.2] ], 20) ))

classes, dim  = 3, 2

def c(d, mu):
    min_dist = np.inf
    min_class = -1
    for c, mu_c in enumerate(mu):
        dist = np.linalg.norm( d - mu_c )
        if dist <= min_dist:
            min_class = c
            min_dist = dist
    return min_class

def classify(data, mu):
    classes = - np.ones(np.size(data,0))
    for i,d in enumerate(data):      
        classes[i] = c(d,mu)
    return classes

def recalculate(data, mu):
    classes = classify(X, mu)
    for i in range(0,np.size(mu,0)):
        data_index = classes == i
        
        data_i = data[data_index]
        if np.size(data_i,0) != 0:
            mu[i,:] = mean(data_i,0)
        
    return mu

def distortion(mu):
    s = 0
    for d in X:
        clazz  = mu[ c(d,mu), :]
        s += sum((d-clazz)**2)
    return s
        
       


def vis(itern, mu):
    C = classify(X,mu)

    figure(); 
    title("Iteration: %d, Distortion: %5.2f" % (itern, distortion(mu)) )
    xlim((0,10)); ylim((0,10))

    scatter(X[:,0], X[:,1],  c=C,  s = 100)
    scatter(mu[:,0], mu[:,1], 200, range(0,classes), marker='+')
    
def vis_paths(mu_hist):
    for t in range(len(mu_hist) - 1):
        mu_cur, mu_next = mu_hist[t], mu_hist[t+1]
            
        for c in range(0,classes):
            cur  = mu_cur[c,:]
            next = mu_next[c,:]

            velo = next - cur
    
            x_cur, y_cur  = cur
            x_next, y_next  = velo

            arrow( x_cur, y_cur, x_next, y_next, fc='k', ec='k', color=cm.hot(c))# head_width=0.1, head_length=0.3)
          #  print(c,":", x_cur, y_cur, x_next, y_next)

            


mu = newClass([3,3], [[10,0],[0,10]], classes)

#figure()
vis(0, mu)
#classify(X,mu)
savefig("000.png")

mu_hist = [mu] 
for n in range(1, 22):
    mu = recalculate(X,mu.copy())  
    mu_hist.append(mu)

    vis(n, mu)
    vis_paths(mu_hist)
    savefig("%03d.png"%n)	

    if (mu_hist[-1] == mu_hist[-2]).all():
        break;

os.system('convert -delay 100 *.png isodata.gif')
os.system('rm *.png')

