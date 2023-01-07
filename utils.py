import numpy as np
import matplotlib.pyplot as plt

# s'' = -MG/s^2
# v = s'
# v' = a = -MG/s^2
# se y = [s(t),v(t)] entao y' = [v(t),-MG/s(t)^2]
def gravitational_acel(d:float,t:float,M:float,G:float):

    return np.array([d[1], -(M*G)/(d[0]**2)])

def rungekutta4(f, y0, t,h, args=()):
    # n = len(t)
    # y = np.zeros((n, len(y0)))
    y = y0
    # print('y0:',y0)
    # print(h)
    k1 = f(y, t, *args)
    # print('[velocidade:',k1[0],'aceleracao:',k1[1],']')
    k2 = f(y + k1 * h / 2., t + h / 2., *args)
    k3 = f(y + k2 * h / 2., t + h / 2., *args)
    k4 = f(y + k3 * h, t + h, *args)
    y = y + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)
    # print('y:',y)
    return y

def plot_space(x,y,origin):

    plt.plot(x, y)
    plt.scatter(*origin,c='y')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()

# t = np.linspace(0,100000,1000)
# rungekutta4(gravitational_acel,np.array([20.0,0.0]),t,(10,10))
