
# coding: utf-8

## Programma per trasporto

### Libraries

# In[1]:

import numpy
import math
import matplotlib.pyplot as plt


### Functions

# In[5]:

def lorentz(E,W,V):
    lor=1/(math.pi*h(1+((V-E)/W)**2))
    lor=W**2/((V-E)**2+W**2)
    return lor


### Parameters

# In[2]:

V_min=-2
V_max=2
Step_size=0.01
V=numpy.arange(V_min,V_max,Step_size)
n_steps=V.size
I=numpy.zeros(n_steps)
dos=numpy.zeros(n_steps)


#### Molecule

# In[3]:

E_homo=+0.5
E_lumo=-0.1
W_homo=0.01
W_lumo=0.01


# In[6]:

dos=numpy.zeros(n_steps)
dos=dos+lorentz(E_homo,W_homo,V)
dos=dos+lorentz(E_lumo,W_lumo,V)


#### Junction

# In[4]:

Alpha_1=0.3
Alpha_2=1-Alpha_1
Gamma_1=1
Gamma_2=0.001
E_block=0


### Main

# In[7]:

plt.plot(V,dos)
plt.show()


# In[ ]:



