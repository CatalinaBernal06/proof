## 
import numpy as np
import matplotlib.pyplot as plt

dat = np.loadtxt('fecha_manchas.dat')
x = dat[:,0]
y = dat[:,1]

plt.figure()
plt.plot(x, y)
plt.savefig('fecha_machas.pdf')
