## IMPORT
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib.colors import LogNorm
import time

## SURFACE

def paraboloid(x, y, a=1, b=1, c=0):
    """
    Surface function: simple paraboloid 
    """
    return a*x**2 + b*y**2 + c

def paraboloid_grad(params, a=1, b=1, c=0):
    """
    Surface gradient
    """
    x      = params[0]
    y      = params[1]
    grad_x = 2*a*x
    grad_y = 2*b*y
    return [grad_x,grad_y]


def weird_paraboloid(x, y, q=6):
    """
    Surface function: f 
    """
    return 1+0.5*q*(x**2+y**2)-np.cos(2*np.pi*(x*y-y**2))

def weird_paraboloid_grad(params, q=6):
    """
    Surface gradient
    """
    x      = params[0]
    y      = params[1]
    grad_x = q*x+2*np.pi*y*np.sin(2*np.pi*(x*y-y**2))
    grad_y = q*y+2*np.pi*(x-2*y)*np.sin(2*np.pi*(x*y-y**2))
    return [grad_x,grad_y]