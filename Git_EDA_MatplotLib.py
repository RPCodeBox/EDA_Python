# In[1]  - Documenation
"""
Script: Git_EDA_MatplotLib.py
Description: EDA Python code for data anlaysis and visualization using MatPlotLib
Author: Rana Pratap
Created: Jan 2021
Version: 1.0
-*- coding: utf-8 -*-
"""
print(__doc__)

# In[1] - Import Libraries
import matplotlib.pyplot as plt
import matplotlib as mt
import numpy as np

# In[2] - Set the data
Years = list(range(2012,2020))
print('Years: ', Years)
Suzuki = [6.8,68.25,222.65,401.64,661.30,1110.70,1200.21,1217.02]
print('Suzuki: ', Suzuki)
Renault = [24.89,46.6,89.27,130.13,150.79,191.43,222.85,216.07]
print('Renault: ', Renault)
Fiat = [15.03,12.38,8.76,16.94,30.71,35.13,26.74,6.94]
print('Fiat: ', Fiat)

# In[3] - Milti line graph plot - Simple
plt.plot(Years,Suzuki,label='Suzuki',c='r',ls='--')
plt.plot(Years,Renault,label='Renault',c='b',ls='-.')
plt.plot(Years,Fiat,label='Fiat',c='g',ls=':')
plt.legend()
plt.show()

# In[4] - Font formatiting for the plot
mt.rcParams['font.size']=12
mt.rcParams['font.family']='sans-serif'
mt.rcParams['font.style']='italic'
mt.rcParams['font.weight']='light'

# In[5] - Milti line graph plot - Medium
plt.figure(figsize=(15,10))
plt.plot(Years,Suzuki,label='Suzuki',c='r',ls='--')
plt.plot(Years,Renault,label='Renault',c='b',ls='-.')
plt.plot(Years,Fiat,label='Fiat',c='g',ls=':')
plt.legend()
plt.show()

# In[6] - Multi line graph plot with customization
plt.figure(figsize=(15,10))
plt.plot(Years,Suzuki,label='Suzuki',lw='2',marker='o',ms=10,c='red')
plt.plot(Years,Renault,label='Renault',lw='2',marker='^',ms=10,c='blue')
plt.plot(Years,Fiat,label='Fiat',lw='2',marker='P',ms=10,c='violet')
plt.title('Vehicle Sales',style='normal',size=24)
plt.grid(color='black',linestyle='-.',linewidth=0.4)
plt.legend()
plt.show()

# In[7] - Insert Graph with annotation
x = np.linspace(0,20,50)
xcos = np.cos(x**2)
xsquare = x**2
fig,ax1 = plt.subplots()
plt.subplots_adjust(left=0.5,right=2,top=1.6,bottom=0)
#Setting the inset plot dimensions
left, bottom, width, height = [0.65, 1, 0.45, 0.35]
inset = fig.add_axes([left,bottom,width,height])
ax1.plot(x,xcos)
inset.plot(x,xsquare,c='red',ls=":")
ax1.annotate('Quadratic Function',xy=(8.1,0.65),xytext=(15,1),fontsize=12,
             fontweight='bold',arrowprops=dict(linewidth=2,arrowstyle='->'),
             rotation=0)
plt.show()
del(x,xcos,xsquare,fig,ax1)

# In[8]:
y=np.arange(100)
ax1 = plt.subplot(221) #Specify 1 - Row 2, Column 2, Index 1
plt.plot(-y*y)
ax2 = plt.subplot(222) #Specify 1 - Row 2, Column 2, Index 2
plt.plot(y*y)
ax3 = plt.subplot(223) #Specify 1 - Row 2, Column 2, Index 2
plt.plot(y*-y)
ax4 = plt.subplot(224) #Specify 1 - Row 2, Column 2, Index 2
plt.plot(-y*-y)
plt.subplots_adjust(left=0.5,right=2,top=5,bottom=3)
plt.show()

# In[9] - Clear Variables
del(Years,Suzuki,Renault,Fiat)
#del(left,right,top,bottom)
del(plt,mt,np)

