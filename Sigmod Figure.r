#Sigmoid function and Linear function 
z <- seq(from = -10, to = 10, by = 0.01)
y = 2*x + 13
g = 1/(1+exp(-y))

library(ggplot2)


p1 <- ggplot(data = NULL, mapping = aes(x = z,y = y))
p1 <- p1 + geom_line(colour = 'blue')

p2 <- ggplot(data = NULL, mapping = aes(x = z,y = g))
p2 <- p2 + geom_line(colour = 'blue')
