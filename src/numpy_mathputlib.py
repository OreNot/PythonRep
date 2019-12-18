import numpy
import matplotlib
from matplotlib.pyplot import figure, plot, xlabel, ylabel, title, show

a = numpy.array([(2, 3, 4), (5, 8, 3)])
z = numpy.zeros((3, 2))
print(a.shape)
print(z)

x = numpy.linspace(0, 5, 10)
y = x ** 2
print(x)
print(y)

figure()
plot(x, y, 'g')
xlabel('x')
ylabel('y')
title('graph')
show()

