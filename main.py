
import numpy as np
import matplotlib.pyplot as plt
from corpus import Corpus
from utils import *

#Constantes
h           = 0.01  #Step size for runge kutta
G           = .01   # Constante de gravidade  CONDIÇÂO DE EQUILIBRIO ACHADA: .01 
Ms          = 2.    #Massa do corpo maior CONDIÇÂO DE EQUILIBRIO ACHADA:2.
Me          = 5.    #Massa do corpo menor CONDIÇÂO DE EQUILIBRIO ACHADA:5.
d0          = 2.    #Distancia entre os corpos CONDIÇÂO DE EQUILIBRIO ACHADA:2
v0      = .01       #velocidade inicial do corpo no eixo y CONDIÇÂO DE EQUILIBRIO ACHADA: .01   
debbuging = False   #True se quiser ver os prints
timespace =  200.0  #Aumentar o número de amostras de tempo

#Corpus
A = Corpus(np.array([0.,0.]),np.array([0.,0.]),Ms) #Corpo imóvel
B = Corpus(np.array([d0,0.]),np.array([0.,v0]),Me) #Corpo móvel

#Array de posições
pos = np.array([B.pos])

for i in range(int(timespace/h)):

    vdist = B.pos - A.pos #Vetor distancia
    dist = np.linalg.norm(vdist) #Modulo
    udist = vdist/dist #Vetor unitário
    
    dist,cntp_vel = rungekutta4(gravitational_acel,[dist,B.cntp_vel],i,h,(G,Ms)) #Distancia no futuro aproximada por Runge kutta
    
    vvel_cntp = udist*cntp_vel #Usa o vetor unitário da distancia * o valor absoluto velocidade pra calcular o vetor velocidade cntp

    B.velocity += vvel_cntp

    B.pos += B.velocity #Soma ao vetor distancia a variação em função da velocidade inicial
    pos = np.append(pos,[B.pos],axis=0) #Array de valores
    if debbuging:
        print('Tempo:',i)
        print('Vetor velocidade centripeta:', vvel_cntp)
        print('Vetor velocidade absoluta:',B.velocity)
        print('Posição:', B.pos)
# print(pos[0:10])
plt.plot(pos[:,0], pos[:,1])
plt.scatter(*A.pos,c='y')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

