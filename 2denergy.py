import matplotlib
import pylab
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
x,y=np.genfromtxt("GAU_AApos_opsh.txt",unpack=True)
BIN_no=50
count,edges_x,edges_y=np.histogram2d(x,y,bins=BIN_no,range=[[-150, 150],[-12, 12]])
print(count)
prob=np.divide(count,x.size)
prob1=np.where(prob==0, 0.0000001, prob) 
print(prob1)
print(prob1.sum())
logv=np.log2(prob1)
g=np.multiply(-0.6,logv)
fig=plt.figure()
ax=fig.add_subplot(title="GAU motif")
cm=ax.pcolormesh(edges_y,edges_x,g)
ax.set_xlabel('Shear' + "(" + r'$\AA$' +")", size=14)
ax.set_ylabel('Open' + "(" + '\N{DEGREE SIGN}' +")", size=14)
fig.colorbar(cm)
plt.savefig("GAU_AApos_opsh_2denergy.tif")
    


