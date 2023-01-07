import numpy as np
import matplotlib.pyplot as plt


# s'' = -MG/s^2
#Transformar essa equalçao num sistema de equações de primeira ordem

# v = s'
# v' = a = -MG/s^2
# Fazendo a substituição esse é o novo sistema
# em coordenadadas fica
# y = [s(t),v(t)] entao y' = [v(t),-MG/s(t)^2]
def gravitational_acel(d:float,t:float,M:float,G:float):

    return np.array([d[1], -(M*G)/(d[0]**2)]) # retorna um array com [velocidade,aceleração] = [s'(t),s''(t)]

def rungekutta4(f, y0, t,h, args=()):
    # n = len(t)
    # y = np.zeros((n, len(y0)))
    y = y0
    # print('y0:',y0)
    # print(h)
    k1 = f(y, t, *args)
    # print('k1:[velocidade:',k1[0],'aceleracao:',k1[1],']')
    k2 = f(y + k1 * h / 2., t + h / 2., *args)
    # print('k2:[velocidade:',k2[0],'aceleracao:',k2[1],']')
    k3 = f(y + k2 * h / 2., t + h / 2., *args)
    # print('k3:[velocidade:',k3[0],'aceleracao:',k3[1],']')
    k4 = f(y + k3 * h, t + h, *args)
    # print('k4:[velocidade:',k4[0],'aceleracao:',k4[1],']')

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

