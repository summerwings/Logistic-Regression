
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

