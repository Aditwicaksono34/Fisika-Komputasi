import matplotlib.pyplot as plt
import time
import numpy as np
import matplotlib.pyplot as plt
jmax = 100
x = 0.0
y = 0.0

for i in range(jmax + 1):
    x += (np.random.random() - 0.5) * 2
    y += (np.random.random() - 0.5) * 2
    xs, ys = line.get_data()
    xs = np.append(xs, [x])
    ys = np.append(ys, [y])
    line.set_data(xs, ys)
    fig.canvas.draw()
    time.sleep(0.1)

print("r actual =", np.sqrt(x ** 2 + y ** 2))
print("r expected =", np.sqrt(jmax) * 0.75)
fig, ax = plt.subplots()
(line,) = plt.plot([0], [0], ".-")
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
plt.show()