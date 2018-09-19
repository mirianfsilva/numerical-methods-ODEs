#Forward Euler 
import math, sys 
import numpy as np

def ForwardEuler(f, y0, T, n):
    """Solve y’= f(y,t), y(0)=y0, with n steps until t=T."""
    t = np.zeros(n+1)
    y = np.zeros(n+1) # y[k] is the solution at time t[k]
    y[0] = y0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        y[k+1] = y[k] + dt*f(y[k], t[k])
    return y, t

# Problem: y'=y
def f(t, y): 
    return y
