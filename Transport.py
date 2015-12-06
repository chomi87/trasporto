
# coding: utf-8

## Programma per trasporto

### Libraries

# In[66]:




# In[67]:



import numpy as np
import math
import matplotlib.pyplot as plt




### Functions

# In[28]:

def lorentz(E,W,V):
    lor=1/(math.pi*(1+((V-E)/W)**2))
    lor=W**2/((V-E)**2+W**2)
    return lor


# In[29]:

def dos_electrodes(bias,a_t,a_s,V):
    n_steps=V.size
    dos=np.zeros(n_steps)
    e_tip=0
    e_sample=0
    
    e_tip=e_tip-(bias*a_t)
    e_sample=e_sample+(bias*a_s)
    
    dos=((V-e_tip)<0)
    return dos


# In[30]:

def dos_electrodes2(bias,a_t,a_s,V):
    n_steps=V.size
    dos=np.zeros(n_steps)
    e_tip=0
    e_sample=0
    K=8.6*math.pow(10, -5)
    T=4.7
    KT=K*T
    
    e_tip=e_tip-(bias*a_t)
    e_sample=e_sample+(bias*a_s)
    
    dos=[1/(np.exp((V-e_tip)/KT)+1),1/(np.exp((V-e_sample)/KT)+1)]
    return dos


### Parameters

# In[31]:

V_min=-2
V_max=2
Step_size=0.001
V=np.arange(V_min,V_max,Step_size)
n_steps=V.size
I=np.zeros(n_steps)
dos=np.zeros(n_steps)


#### Molecule

# In[32]:

E_homo=+0.5
E_lumo=-0.1
W_homo=0.01
W_lumo=0.01


# In[33]:

dos=np.zeros(n_steps)
dos=dos+lorentz(E_homo,W_homo,V)
dos=dos+lorentz(E_lumo,W_lumo,V)


#### Junction

# In[ ]:

Alpha_1=0.3
Alpha_2=1-Alpha_1
Gamma_1=1
Gamma_2=0.001
E_block=0
electrodes=dos_electrodes2(0.5,Alpha_1,Alpha_2,V)


### Main

# In[44]:

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


#### ANIMAZIONE

# In[73]:

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(V_min, V_max), ylim=(-0.5, 2))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    KT=0.00001
    e_tip=0
    x = np.linspace(V_min, V_max, n_steps)
    y = 1/(np.exp((V-(e_tip-((V_min+i*Step_size*10)*Alpha_1)))/KT)+1)
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=n_steps/10, interval=1)

plt.show()


### ESEMPI DI ANIMAZIONI MULTIPLE ALTRUI

#### PRIMO

# In[74]:

from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()

ax = plt.axes(xlim=(0, 2), ylim=(0, 100))

N = 4
lines = [plt.plot([], [])[0] for _ in range(N)]

def init():    
    for line in lines:
        line.set_data([], [])
    return lines

def animate(i):
    for j,line in enumerate(lines):
        line.set_data([0, 2], [10 * j,i])
    return lines

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20)

plt.show()


#### SECONDO

# In[108]:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation


# This example uses subclassing, but there is no reason that the proper
# function couldn't be set up and then use FuncAnimation. The code is long, but
# not really complex. The length is due solely to the fact that there are a
# total of 9 lines that need to be changed for the animation as well as 3
# subplots that need initial set up.
class SubplotAnimation(animation.TimedAnimation):
    def __init__(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 2, 1)
        ax2 = fig.add_subplot(2, 2, 2)
        ax3 = fig.add_subplot(2, 2, 4)

        self.t = np.linspace(0, V_max, n_steps)
        #self.t = np.linspace(0, 80, 400)

        e_tip=0
        e_sample=0
        KT=1
        self.y=1/(np.exp((V-(e_tip-((self.t*Step_size*10)*Alpha_1)))/KT)+1)
        #self.x = np.cos(2 * np.pi * self.t / 10.)
        self.x = np.sin(2 * np.pi * self.t / 10.)
        self.z = 1/(np.exp((V-(e_sample-((self.t*Step_size*10)*Alpha_2)))/KT)+1)
        #self.z = 10 * self.t

        ax1.set_xlabel('x')
        ax1.set_ylabel('y')
        self.line1 = Line2D([], [], color='black')
        self.line1a = Line2D([], [], color='red', linewidth=2)
        self.line1e = Line2D(
            [], [], color='red', marker='o', markeredgecolor='r')
        ax1.add_line(self.line1)
        ax1.add_line(self.line1a)
        ax1.add_line(self.line1e)
        #ax1.set_xlim(-1, 1)
        #ax1.set_ylim(-2, 2)
        ax1.set_xlim(V_min, V_max)
        ax1.set_ylim(-0.25, 1.5)
        
        #ax1.set_aspect('equal', 'datalim')

        ax2.set_xlabel('bias')
        ax2.set_ylabel('tip')
        self.line2 = Line2D([], [], color='black')
        self.line2a = Line2D([], [], color='red', linewidth=2)
        self.line2e = Line2D(
            [], [], color='red', marker='o', markeredgecolor='r')
        ax2.add_line(self.line2)
        ax2.add_line(self.line2a)
        ax2.add_line(self.line2e)
        ax2.set_xlim(V_min, V_max)
        ax2.set_ylim(-0.25, 1.25)

        ax3.set_xlabel('bias')
        ax3.set_ylabel('sample')
        self.line3 = Line2D([], [], color='black')
        self.line3a = Line2D([], [], color='red', linewidth=2)
        self.line3e = Line2D(
            [], [], color='red', marker='o', markeredgecolor='r')
        ax3.add_line(self.line3)
        ax3.add_line(self.line3a)
        ax3.add_line(self.line3e)
        ax3.set_xlim(V_min, V_max)
        ax3.set_ylim(-0.25, 1.25)

        animation.TimedAnimation.__init__(self, fig, interval=50)

    def _draw_frame(self, framedata):
        i = framedata
        head = i - 1
        head_len = 10
        head_slice = (self.t > self.t[i] - 1.0) & (self.t < self.t[i])

        self.line1.set_data(self.t[:i], self.x[:i])
        self.line1.set_data(self.t[:i], self.x[:i])
        self.line1a.set_data(self.t[head_slice], self.x[head_slice])
        self.line1e.set_data(self.t[head], self.x[head])

        self.line2.set_data(self.t[:i], self.y[:i])
        self.line2a.set_data(self.t[head_slice], self.y[head_slice])
        self.line2e.set_data(self.t[head], self.y[head])

        self.line3.set_data(self.t[:i], self.z[:i])
        self.line3a.set_data(self.t[head_slice], self.z[head_slice])
        self.line3e.set_data(self.t[head], self.z[head])

        self._drawn_artists = [self.line1, self.line1a, self.line1e,
                               self.line2, self.line2a, self.line2e,
                               self.line3, self.line3a, self.line3e]

    def new_frame_seq(self):
        return iter(range(self.t.size))

    def _init_draw(self):
        lines = [self.line1, self.line1a, self.line1e,
                 self.line2, self.line2a, self.line2e,
                 self.line3, self.line3a, self.line3e]
        for l in lines:
            l.set_data([], [])

ani = SubplotAnimation()

plt.show()


#### Terzo

# In[64]:


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(V_min, V_max), ylim=(-0.5, 2))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
     y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y[0])
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html

plt.show()

