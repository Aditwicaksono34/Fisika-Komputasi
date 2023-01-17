import numpy as np

a = 0
b = np.pi
n = 11
h = (b - a) / (n - 1)
x = np.linspace(a, b, n)
f = np.sin(x)

I_riemannL = h * sum(f[:n-1])
err_riemannL = 2 - I_riemannL

I_riemannR = h * sum(f[1::])
err_riemannR = 2 - I_riemannR

I_mid = h * sum(np.sin((x[:n-1]+x[1:])/2))
err_mid = 2 - I_mid

print("integral kiri: ", I_riemannL)
print("error kiri: ", err_riemannL)

print("integral kanan: ", I_riemannR)
print("error kanan: ", err_riemannR)

print("integral tengah: ", I_mid)
print("error integral tengah: ", err_mid)