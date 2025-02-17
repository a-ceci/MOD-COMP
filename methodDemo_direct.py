#The current script is an example on computing properties for
#a compressible boundary layer using the method described in
#Hasan et al. (https://doi.org/10.2514/1.J063335),
#but with additional modular features as seen in compressibleBLprofiles
#detailed further in Kumar & Larsson (https://doi.org/10.2514/1.J061735)

#Here, we compute the boundary layer properties using the default modeling choices. 
#For more information, see README file

import os
import sys

# add path to BL libraries
pwd      = os.getcwd()
pathfuns = pwd+'/src'
sys.path.append(pathfuns)

#import Python libraries
import boundaryLayerPropFunctions_direct as funs
import matplotlib.pyplot as plt

#define properties for compressible boundary layer
M = 5           #Mach number
ReDelta2 = 3000 #Reynolds number
Tw = 300        #Wall temperature
Te = 200        #Freestream temperature
Tw_Te = Tw/Te   #Ratio of wall to freestream temperature
N = 500         #number of grid points in the boundary layer

[cf,Bq,ch,yPlus,uPlus,Tplus,mu_muw,kappa_VK] = funs.boundaryLayerProperties(M,ReDelta2,Tw_Te,Te,N)

#print quantities
print('\n')
print('cf = '+str(cf))  #skin-friction coefficient
print('\n')
print('Bq = '+str(Bq))  #Wall heat transfer rate
print('\n')
print(f'ch = {ch}')     #Stanton number
print('\n')

#create plots
fig1,axs1 = plt.subplots()
axs1.plot(yPlus,uPlus)  #Velocity profile
axs1.set_xscale('log')
axs1.set_xlabel('$y^+$')
axs1.set_ylabel('$u^+$')
axs1.set_title('Boundary layer velocity profile')
axs1.set_xlim(left = 0.1)

fig2,axs2 = plt.subplots()
axs2.plot(yPlus,Tplus)  #Temperature profile
axs2.set_xscale('log')
axs2.set_xlabel('$y^+$')
axs2.set_ylabel('$T^+$')
axs2.set_title('Boundary layer temperature profile')
axs2.set_xlim(left = 0.1)

plt.show()
