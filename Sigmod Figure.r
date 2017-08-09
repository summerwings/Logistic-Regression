#Sigmoid function 
z <- seq(from = -10, to = 10, by = 0.01)
y = 1/(1+exp(-z))

library(ggplot2)

p <- ggplot(data = NULL, mapping = aes(x = z,y = y))
p + geom_line(colour = 'blue')
