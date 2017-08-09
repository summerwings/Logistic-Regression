# Linear decision boundary 
import random
from numpy import loadtxt, where  
from pylab import scatter, show, legend, xlabel, ylabel
  
X = 10*[random.random(1,3)] + 10*[random.random(3,6)]
y = [1]*10 + [0]*10  
  
pos = where(y == 1)  
neg = where(y == 0)  
scatter(X[pos, 0], X[pos, 1], marker='o', c='b')  
scatter(X[neg, 0], X[neg, 1], marker='x', c='r')  
show()  
