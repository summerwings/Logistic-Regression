from numpy import arange,array
from pylab import scatter, plot, show

# Gradient Descent

# generate Y=-X**2 - 3X - 2
X = arange(-4.5, 1.5,.01)
Y1 = [-(abs(i)**2) for i in X]
Y2 = [-(3*i+2) for i in X]
Y = map(lambda(Y1,Y2): Y1 + Y2,zip(Y1,Y2))

x =  arange(-3, -1,.5)
y = []

for i in x:
    y.append(-(2*i**2 + 6*i + 4.25))

# plot
scatter(X,Y,c='g')
plot(x,y,marker='x',c='b')

show()
