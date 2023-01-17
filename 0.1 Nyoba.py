from vpython import*
import numpy as np

Plot1=gcurve(color=color.white)

for x in arange(0., 8.1, 0.1):
    Plot1.plot(pos=(x,5*np.cos(2.*x)*exp(-0.4*x)))

graph1= graph(width=600, height=450, title='Visualisasi 2D', xtitle='x', ytitle='f(x)', foreground=color.black, background=color.white)

Plot2=gdots(color=color.black)

for x in arange(-5., +5, 0.1):
    Plot2.plot(pos=(x,cos(x)))
