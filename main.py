
import numpy as np
import matplotlib.pyplot as plt
from corpus import Corpus
from utils import *

#Constantes
G           = 6.67e-11                  # constant G
Ms          = 2.0e30                    # sun
Me          = 5.972e24                  # earth        
AU          = 1.5e13                    # earth sun distance
daysec      = 24.0*60*60                # seconds of a day
e_ap_v      = 29290                     # earth velocity at aphelion

#Corpus
A = Corpus(np.array([0,0]),np.array([0,0]),Ms) #Corpo imóvel
B = Corpus(np.array([AU,0]),np.array([0,e_ap_v]),Me) #Corpo móvel


timespace = np.linspace(0,100000000,100) #Aumentar o número de amostras aumenta a precisão, aumentar o intervalo aumenta a janela

pos = np.array([B.pos])


for i in range(len(timespace)-1):
    # print('Tempo:',t)
    vdist = B.pos - A.pos #Vetor distancia
    dist = np.linalg.norm(vdist) #Modulo
    udist = vdist/dist #Vetor unitário
    h = timespace[i+1] - timespace[i]
    print(gravitational_acel(dist,G,Ms))
    dist,B.cntp_vel = rungekutta4(gravitational_acel,[dist,B.cntp_vel],timespace[i],h,(G,Ms))
    
    vdist = udist*dist
    
    B.pos = vdist + B.velocity
    
    # print('vetor distancia:',vdist)
    # print('pos:',B.pos)
    pos = np.append(pos,[B.pos],axis=0)

print(pos[0:10])
# print(pos)
plot_space(pos[:,0],pos[:,1],A.pos)
