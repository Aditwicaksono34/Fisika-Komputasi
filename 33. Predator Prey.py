import vpython
from vpython import*
import matplotlib.pyplot as plt
import numpy as np

Tmin=0.0
Tmax=500.0
y=np.zeros((2), float)
Ntimes=1000
y[0]=2.0
y[1]=1.3
h=(Tmax-Tmin)/Ntimes
t=Tmin

def f(t,y,F):
    F[0]=0.2*y[0]*(1-(y[0]/[20.0]))-0.1*y[0]*y[1]
    F[1]=-0.1*y[1]+0.1*y[0]*y[1]
def rk4(t,y,h,Neqs):
    F = np.zeros((Neqs),float)
    ydumb = np.zeros((Neqs),float)
    k1 =np.zeros((Neqs),float)
    k2 = np.zeros((Neqs),float)
    k3 = np.zeros((Neqs), float)
    k4 = np.zeros((Neqs), float)
    f(t,y,F)
    for i in range(0,Neqs):
        k1[i]=h*F[i]
        ydumb[i]=y[i]+k1[i]/2.
    f(t+h/2.,ydumb,F)
    for i in range(0,Neqs):
        k2[i]=h*F[i]
        ydumb[i]=y[i]+k2[i]/2.
    f(t+h/2.,ydumb,F)
    for i in range(0,Neqs):
        k3[i]=h*F[i]
        ydumb[i]=y[i]+k3[i]/2.
    f(t+h/2.,ydumb,F)
    for i in range(0,Neqs):
        k4[i]=h*F[i]
        ydumb[i]=y[i]+k4[i]/2.
    f(t+h/2.,ydumb,F)
    for i in range(0, Neqs):
        k4[i]=h*F[i]
        y[i]=y[i]+(k1[i]+2.*(k2[i]+k3[i]+k4[i]))/6.

graph1=graph(x=0,y=0, width=500, height=400, title='Prey p(green) and Predator P (yellow) vs time',\
               xtitle='t', ytitle='P, p', xmin=0, xmax=500, ymin=0, ymax= 3.5)
funct1=gcurve(color=color.yellow)
funct2=gcurve(color=color.green)
graph2=graph(x=0, y=400, width=500, height=400, tittle = "Predator P Vs prey p", xtitle="P", ytitle='p', xmin=0, xmax= 2.5, ymin=0, ymax= 3.5)
funct3=gcurve(color=color.red)

for t in arange(Tmin, Tmax+1, h):
    funct1.plot(pos=(t,y[0]))
    funct2.plot(pos=(t,y[1]))
    funct3.plot(pos=(y[0],y[1]))
    rate(60)
    rk4(t,y,h,2)