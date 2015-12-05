
# coding: utf-8

## Programma per trasporto

### Libraries

# In[97]:

import numpy
import math
import matplotlib.pyplot as plt


### Functions

# In[98]:

def lorentz(E,W,V):
    lor=1/(math.pi*(1+((V-E)/W)**2))
    lor=W**2/((V-E)**2+W**2)
    return lor


# In[99]:

def dos_electrodes(bias,a_t,a_s,V):
    n_steps=V.size
    dos=numpy.zeros(n_steps)
    e_tip=0
    e_sample=0
    
    e_tip=e_tip-(bias*a_t)
    e_sample=e_sample+(bias*a_s)
    
    dos=((V-e_tip)<0)
    return dos


# In[100]:

def dos_electrodes2(bias,a_t,a_s,V):
    n_steps=V.size
    dos=numpy.zeros(n_steps)
    e_tip=0
    e_sample=0
    K=8.6*math.pow(10, -5)
    T=4.7
    KT=K*T
    
    e_tip=e_tip-(bias*a_t)
    e_sample=e_sample+(bias*a_s)
    
    dos=[1/(numpy.exp((V-e_tip)/KT)+1),1/(numpy.exp((V-e_sample)/KT)+1)]
    return dos


### Parameters

# In[101]:

V_min=-2
V_max=2
Step_size=0.001
V=numpy.arange(V_min,V_max,Step_size)
n_steps=V.size
I=numpy.zeros(n_steps)
dos=numpy.zeros(n_steps)


#### Molecule

# In[102]:

E_homo=+0.5
E_lumo=-0.1
W_homo=0.01
W_lumo=0.01


# In[103]:

dos=numpy.zeros(n_steps)
dos=dos+lorentz(E_homo,W_homo,V)
dos=dos+lorentz(E_lumo,W_lumo,V)


#### Junction

# In[107]:

Alpha_1=0.3
Alpha_2=1-Alpha_1
Gamma_1=1
Gamma_2=0.001
E_block=0
electrodes=dos_electrodes2(0,Alpha_1,Alpha_2,V)


### Main

# In[109]:

f, axarr = plt.subplots(3, sharex=True)
axarr[0].plot(V, dos, color='r')
axarr[0].fill_between(V,dos,0,where=V<0,color='r')

axarr[0].set_title('Molecule dos')

axarr[1].plot(V, electrodes[0],color='g')
axarr[1].fill_between(V,electrodes[0],0,color='g')
axarr[1].set_title('Tip dos')

axarr[2].plot(V, electrodes[1],color='b')
axarr[2].fill_between(V,electrodes[1],0,color='b')
axarr[2].set_title('Sample dos')


plt.show()


# In[ ]:




# In[ ]:




# In[96]:




# In[96]:




# In[77]:




# In[ ]:



