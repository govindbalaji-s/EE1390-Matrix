import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.ticker.EngFormatter
fig = plt.figure()

xvals = np.arange(-7.5, 7.5, 0.01)
r5 = np.sqrt(5)
yparabola_u = np.sqrt(4*xvals)
yparabola_d = -1*yparabola_u
ydirectrix = xvals * 0 + -1
yline = 2*xvals + 1
ytan1 = -0.618033988749895 * xvals - 1.61803398874989
ytan2 =  1.61803398874989 * xvals + 0.618033988749895

ptinter = np.array([-1, -1])
ptP=np.array([(3+np.sqrt(5))/2, -np.sqrt(5)-1])
ptQ=np.array([(3-np.sqrt(5))/2, np.sqrt(5)-1])

plt.plot(xvals, yparabola_u, label = "$y^2=4ax$")
plt.plot(xvals, yparabola_d, label = "$y^2=4ax$")
#plt.plot(xvals, ydirectrix, label="$x=-a$")
plt.plot(np.arange(-15, 15, 0.01)*0-1, np.arange(-15, 15, 0.01), label = "$x=-a$")

plt.plot(xvals, yline, label = "$y=2x+a$")
plt.plot(xvals, ytan2, label = r"$y=\frac{2}{\sqrt{5}-1}x + \frac{\sqrt{5} -1}{2}a$")
plt.plot(xvals, ytan1, label = r"$y=\frac{-2}{\sqrt{5}+1}x - \frac{\sqrt{5} +1}{2}a$")

plt.plot(0,0, '.')
plt.plot(ptinter[0], ptinter[1], 'o')
plt.plot(ptP[0], ptP[1], 'o')
plt.plot(ptQ[0], ptQ[1], 'o')

#plt.text(ptinter[0], ptinter[1], 'o')
plt.text(ptP[0], ptP[1], 'P')
plt.text(ptQ[0], ptQ[1], 'Q')

dist = np.linalg.norm(ptP-ptQ)

plt.plot([ptP[0], ptQ[0]], [ptP[1], ptQ[1]], label = "PQ")
plt.text(2, 0, "Distance = $"+str(dist)
    +"a$")
plt.xlabel('$x / a$')
plt.ylabel('$y / a$')
plt.grid()
plt.legend()
plt.show()
