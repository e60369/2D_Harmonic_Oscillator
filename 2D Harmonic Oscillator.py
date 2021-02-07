#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

# parameters
g = 9.81
A = 1
B = 2
phi = math.pi/3
omega = 0.5
dt = 0.01

# add your solution below
z0 = float(input())
total_steps = int((math.sqrt((2*z0)/g))/dt)+2
trajectory =[]
total_t = []
t = 0
x = 0
y = 0
z = 0

for i in range (total_steps):
    t = i*dt
    x = A*math.cos(omega*t)
    y = B*math.cos(omega*t + phi)
    z = (-(1/2)*g*t*t)+ z0
    r = [x,y,z]
    trajectory.append(r)
    total_t.append(t)

t_contact = total_t[-1]
x_contact = A*math.cos(omega*total_t[-1])
y_contact = B*math.cos(omega*total_t[-1] + phi)
z_contact = (-(1/2)*g*t_contact*total_t[-1])+ z0

x_values = [r[0] for r in trajectory]
y_values = [r[1] for r in trajectory]

x_total = sum(x_values)
x_avg = x_total/(len(trajectory))

y_total = sum(y_values)
y_avg = y_total/(len(trajectory))


center = [x_avg,y_avg]
ctr_fmt = [round(elem,3) for elem in center]

print("t_contact = {:.3f}".format(t_contact))
print("x_contact = {:.3f}".format(x_contact))
print("y_contact = {:.3f}".format(y_contact))
print("z_contact = {:.3f}".format(z_contact))
print('center =',ctr_fmt)

