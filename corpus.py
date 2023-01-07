
import numpy as np
import matplotlib.pyplot as plt

class Corpus():
    
    def __init__(self,init_pos:np.array,init_vel:np.array,mass:float):
        self.pos = init_pos.copy()
        self.velocity = init_vel.copy()
        self.mass = mass
        self.cntp_vel = 0

    def set_cntp_vel(self,vel):
        self.cntp_vel = vel


