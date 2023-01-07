
import numpy as np
import matplotlib.pyplot as plt
from corpus import Corpus
from utils import *

#Constantes
G           = .01                 # constant G
Ms          = 2.                    # sun
Me          = 5.                 # earth        
AU          = 2                  # earth sun distance
e_ap_v      = .02                     # earth velocity at aphelion

#Corpus
A = Corpus(np.array([0.,0.]),np.array([0.,0.]),Ms) #Corpo imóvel
B = Corpus(np.array([AU,0.]),np.array([0.,e_ap_v]),Me) #Corpo móvel

timespace =  230#Aumentar o número de amostras
pos = np.array([B.pos])

for i in range(timespace):
    # print('Tempo:',t)
    vdist = B.pos - A.pos #Vetor distancia
    dist = np.linalg.norm(vdist) #Modulo
    udist = vdist/dist #Vetor unitário
    h = 0.1
    dist,cntp_vel = rungekutta4(gravitational_acel,[dist,B.cntp_vel],i,h,(G,Ms)) #Distancia no futuro aproximada por Runge kutta
    
    vvel_cntp = udist*cntp_vel #Usa o vetor unitário da distancia * o valor absoluto velocidade pra calcular o vetor velocidade cntp
    print('oi ', vvel_cntp)
    B.velocity += vvel_cntp
    print(B.velocity)
    B.pos += B.velocity #Soma ao vetor distancia a variação em função da velocidade inicial
    pos = np.append(pos,[B.pos],axis=0) #Array de valores

# print(pos[0:10])
plt.plot(pos[:,0], pos[:,1])
plt.scatter(*A.pos,c='y')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

