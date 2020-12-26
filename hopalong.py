# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 00:19:50 2020

@author: Louie
"""

import numpy as np
import random as rand
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D
from mayavi.mlab import *

import imageio
import matplotlib.cm as cm
from matplotlib import colors


def gif():
    """turns images in the folder frames_path into a gif"""
    n=488
    gif_path = "animation2.gif"
    frames_path = "./imagess/{i}.png"
    with imageio.get_writer(gif_path, mode='I') as writer:
        for i in range(1,200):
            writer.append_data(imageio.imread(frames_path.format(i=i)))
    
def points(n,scale):
    x=np.random.uniform(0,1,n)/scale
    y=np.random.uniform(0,1,n)/scale
    return x,y

def transform(x,y,a=2,b=2.5,c=2,d=0.25):
    x_new=np.sin(a*y)-np.cos(b*x)
    y_new=np.sin(c*x)-np.cos(d*y)
    return x_new,y_new


def transform_3d(x,y,z,a=2,b=2.5,c=2,d=0.25,e=1.5,f=2):
    x_new=np.sin(a*y)-np.cos(b*x)- np.sin(e*z)
    y_new=np.sin(c*x)-np.cos(d*y)+ np.sin(f*z)
    z_new=np.sin(c*x)-np.cos(d*y)- np.sin(e*z)
    return x_new,y_new,z_new


def plot(x,y,name="test"):
    plt.figure(1)
    fig = plt.figure()
    plt.clf()
    fig = plt.gcf()
    fig.set_size_inches(19.2,10.8)
    plt.axis('off')
    plt.style.use('dark_background')
    plt.scatter(x,y,color="white",alpha=0.03,s=1)
    plt.savefig("%s"%(name),dip=150)



    
def plot3d(x,y,z):
    """uses mayavi for a fast interactive 3d plot"""
    points3d(x, y, z,color=(1,1,1),opacity=0.09,mode='point')
    
def run(n,m,scale,a=2,b=2.5,c=2,d=0.25,e=1.5,f=0.5,threeD=False):
    """runs the transform m times on an array of n numbers, plots the final
       distribution.
    """
    s=time.time()
    if not threeD:
        x,y=points(n,scale)
        count=0
        X=np.zeros(n)
        Y=np.zeros(n)
        while count<m:
            x,y=transform(x,y,a,b,c,d)              
            count=count+1  
            #plot(x,y)    #plot here if you wish to see the trasient states
        #plot(x,y)
        plot_hist(x,y)
    if threeD:
        x,y=points(n,scale)
        z=np.random.uniform(0,1,n)/scale
        count=0
        X=np.zeros(n)
        Y=np.zeros(n)
        while count<m:
            x,y,z=transform_3d(x,y,z,a,b,c,d,e,f)  
            count=count+1  
        plot(x,y)    
        
   
    #plot3d(x,y,z)
    print(time.time()-s)


def animate(n,m,scale,frames):
    """use if you want to smoothly vary params of transform"""
    a=np.linspace(0,10,frames)
    b=np.linspace(0,12,frames)
    c=np.linspace(0,10,frames)
    d=np.linspace(0,4,frames)
    x,y=points(n,scale)
    for i in range(frames):
        temp_x=x
        temp_y=y
        s=time.time()
        count=0
        while count<m:
            temp_x,temp_y=transform(temp_x,temp_y,a[i],b[i],c[i],d[i])
            count=count+1 
        plot(temp_x,temp_y,i)
        
        
#animate(100000,100,100,10)
run(1000000,100,100)
#gif()