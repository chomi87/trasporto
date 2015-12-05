
# coding: utf-8

## Programma per trasporto

### Libraries

# In[8]:

import numpy
import math
import matplotlib.pyplot as plt


### Functions

# In[15]:

def lorentz(E,W,V):
    lor=1/(math.pi*(1+((V-E)/W)**2))
    lor=W**2/((V-E)**2+W**2)
    return lor


# In[16]:

def dos_electrodes(bias,a_t,a_s,V):
    n_steps=V.size
    dos=numpy.zeros(n_steps)
    e_tip=0
    e_sample=0
    
    e_tip=e_tip-(bias*a_t)
    e_sample=e_sample+(bias*a_s)
    
    dos=((V-e_tip)<0)
    return dos


# In[60]:

def dos_electrodes2(bias,a_t,a_s,V):
    n_steps=V.size
    dos=numpy.zeros(n_steps)
    e_tip=0
    e_sample=0
    
    e_tip=e_tip-(bias*a_t)
    e_sample=e_sample+(bias*a_s)
    
    dos=1/(numpy.exp((V-e_tip)/0.0001)+1)
    return dos


### Parameters

# In[51]:

V_min=-2
V_max=2
Step_size=0.01
V=numpy.arange(V_min,V_max,Step_size)
n_steps=V.size
I=numpy.zeros(n_steps)
dos=numpy.zeros(n_steps)


#### Molecule

# In[18]:

E_homo=+0.5
E_lumo=-0.1
W_homo=0.01
W_lumo=0.01


# In[19]:

dos=numpy.zeros(n_steps)
dos=dos+lorentz(E_homo,W_homo,V)
dos=dos+lorentz(E_lumo,W_lumo,V)


#### Junction

# In[20]:

Alpha_1=0.3
Alpha_2=1-Alpha_1
Gamma_1=1
Gamma_2=0.001
E_block=0


### Main

# In[63]:

tip=dos_electrodes2(1,Alpha_1,Alpha_2,V)
plt.plot(V,tip)
plt.fill_between(V,tip,0,color='0.8')
plt.show()


# In[62]:




# In[ ]:



