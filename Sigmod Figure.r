library(ggplot2)
x <- seq(from = -10, to = 10, by = 0.01)
#standard Sigmoid function
g = 1/(1+exp(-x))
p0 <- ggplot(data = NULL, mapping = aes(x = x,y = g))
p0 <- p0 + geom_line(colour = 'blue')

#transform Linear function to Sigmoid function
x <- seq(from = -10, to = 10, by = 0.01)
y = 2*x + 13
g = 1/(1+exp(-y))

p1 <- ggplot(data = NULL, mapping = aes(x = x,y = y))
p1 <- p1 + geom_line(colour = 'blue')

p2 <- ggplot(data = NULL, mapping = aes(x = x,y = g))
p2 <- p2 + geom_line(colour = 'blue')
