
# Linear decision boundary(Y= - X + 3) 

import random
from numpy import where
from pylab import scatter, show

x = []
y = []
x0 = []
y0 = []
x1 = []
y1 = []

# generate
for i in range(1000):
    x.append(random.uniform(0,6))
    y.append(-random.uniform(0,6)+3)

# classify    
for i in range(1000):
    if -x[i] + 3 <= y[i]:
        x0.append(x[i])
        y0.append(y[i])
    else:
        x1.append(x[i])
        y1.append(y[i])

# plot        
scatter(x0,y0,marker='o',c='b')
scatter(x1,y1,marker='x',c='r')
Y = [-i + 3 for i in range(6)]
plot(range(6),Y )
show()  

# Non-inear decision boundary(Y= - X + 3) 
import random
from numpy import arange
from pylab import scatter, plot, show

x = []
y = []
x0 = []
y0 = []
x1 = []
y1 = []

# generate
for i in range(500):
    x.append(random.uniform(-2,2))
    y.append(abs(1-abs(random.uniform(-2,2)) ** 2) ** 0.5)

for i in range(500):
    x.append(random.uniform(-2,2))
    y.append(-abs(1-abs(random.uniform(-2,2)) ** 2) ** 0.5)
    


# classify    
for i in range(1000):
    if - abs(1-abs(x[i]) ** 2) ** 0.5 <= y[i] <= abs(1-abs(x[i]) ** 2) ** 0.5 and -1 <= x[i] <= 1:
        x0.append(x[i])
        y0.append(y[i])
    else:
        x1.append(x[i])
        y1.append(y[i])

# plot        
scatter(x0,y0,marker='o',c='b')
scatter(x1,y1,marker='x',c='r')

X = arange(-1, 1.01,.01)
Y1 = [- abs(1-abs(i) ** 2) ** 0.5 for i in X]
Y2 = [abs(1-abs(i) ** 2) ** 0.5 for i in X]
plot(X,Y1,c='g')
plot(X,Y2,c='g')
show()  
