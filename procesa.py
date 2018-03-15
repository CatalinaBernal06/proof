## 
import numpy as np

datos = np.loadtxt('monthrg.dat')
n = datos[:,3]
time = datos[:,0] + (datos[:,1]-1)/12

ii = time>=1900
	
data = np.array([time[ii], n[ii]])		
		
np.savetxt('fecha_manchas.dat', data.T)

