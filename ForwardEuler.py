#Forward Euler 
import math, sys 
import numpy as np

def ForwardEuler(f, t0, y0, T, n, dt):
    """Solve y'=f(t,y), y(0)=y0, with n steps until t=T."""
    if dt == -1:
        dt = (T-t0)/float(n)
    else:
        n = int(math.ceil((T-t0)/dt))
    t = np.zeros(n+1)
    y = np.zeros(n+1)  # y[k] is the solution at time t[k]
    y[0] = y0
    t[0] = t0
    for k in range(n):
        t[k+1] = t[k] + dt
        y[k+1] = round(y[k] + dt*f(t[k], y[k]), 8)
    return t, y

# Problem: y'=y
def f(t, y): 
    return y
