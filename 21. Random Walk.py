import random
random.seed(None)
import vpython as vp
import matplotlib.pyplot as plt
import time
import numpy as np
import vpython as vp

jmax = 100
x = 0.0
y = 0.0
pts = vp.gcurve()
pts.plot(pos=(x,y))

for i in range(0, jmax+1):
    x += (random.random() - 0.5)*2
    y += (random.random() - 0.5)*2
    pts.plot(pos=(x,y))
    vp.rate(5)

fig, ax = plt.subplots()
line, = plt.plot([0], [0], '.-')
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
plt.show()

jmax = 100
x = 0.0
y = 0.0
plt.ion()

for i in range(0, jmax+1):
    x += (random.random() - 0.5)*2
    y += (random.random() - 0.5)*2
    xs, ys = line.get_data()
    xs = np.append(xs, [x])
    ys = np.append(ys, [y])
    line.set_data(xs, ys)
    time.sleep(.2)
    print(i, end=" ")