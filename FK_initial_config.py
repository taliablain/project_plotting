import matplotlib.pyplot
import matplotlib.pyplot as plt
import seaborn as sns
import numpy
from sympy import Matrix

#plt.style.use(['science', 'nature', 'vibrant', 'no-latex'])
plt.rcParams["font.family"] = 'Times New Roman'

p1x = int(0)
p1y = int(0)
p1z = int(0)
p1 = Matrix([0, 0, 0])

p2x = int(500)
p2y = int(0)
p2z = int(1045)
p2 = Matrix([p2x, p2y, p2z])

p3x = int(500)
p3y = int(0)
p3z = int(2345)
p3 = Matrix([p3x, p3y, p3z])

p4x = int(1210)
p4y = int(0)
p4z = int(2290)
p4 = Matrix([p4x, p4y, p4z])

p5x = int(1525)
p5y = int(0)
p5z = int(2290)
p5 = Matrix([p5x, p5y, p5z])

p6x = int(1815)
p6y = int(0)
p6z = int(2290)
p6 = Matrix([p6x, p6y, p6z])

soa = numpy.array([p1, p2, p3, p4, p5], dtype=object)
X, Y, Z = zip(*soa)
X = numpy.array(X)
Y = numpy.array(Y)
Z = numpy.array(Z)
X = numpy.ndarray.flatten(X)
Y = numpy.ndarray.flatten(Y)
Z = numpy.ndarray.flatten(Z)
#p6x, p6y, p6z = zip(*soa)
#p6x = numpy.array(p6x)
#p6y = numpy.array(p6y)
#p6z = numpy.array(p6z)
#p6x = numpy.ndarray.flatten(p6x)
#p6y = numpy.ndarray.flatten(p6y)
#p6z = numpy.ndarray.flatten(p6z)





fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
matplotlib.pyplot.xticks(fontsize=9)

ax.set_xlim([-2000, 2000])
ax.set_ylim([-1500, 2000])
ax.set_zlim([-1500, 2500])

ax.plot3D(X, Y, Z, 'darkorange', marker="o")
ax.plot3D(p6x, p6y, p6z, 'red', marker="^")


matplotlib.pyplot.draw()
matplotlib.pyplot.show()