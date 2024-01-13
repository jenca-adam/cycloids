import numpy as np
from math import sin, cos
FSTEP=.001
class Coor:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self,other):
        return self.__class__(other.x+self.x,other.y+self.y)
    
    def get_pos(self,t):
        return self # don't move
    
    def plot(self,canvas,color=(255,255,255)):
        try:
            canvas[round(self.y%canvas.shape[0]),round(self.x%canvas.shape[1])] = color
        except IndexError:pass
class Spin:
    def __init__(self,r,speed,initrot,parent):
        self.r=r
        self.initrot=initrot
        self.parent=parent
        self.history=[]
        self.speed=speed/1000 #mrad/t
    def get_pos(self,t):
        return to_cartesian((self.speed*t+self.initrot,self.r))+self.parent.get_pos(t) #if there are too many rotations we might have to do this iteratively
    def get_dpos(self,st,dt):
        return [self.get_pos(t) for t in np.arange(st,st+dt,FSTEP)]
def create_canvas(width,height):
    return np.zeros((width,height,3),np.uint8) # rgb

def to_cartesian(polar):
    angle, r = polar
    return Coor(cos(angle)*r, sin(angle)*r)


