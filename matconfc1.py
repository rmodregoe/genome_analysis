# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:12:35 2022

@author: richi
"""
import numpy as np
bases=['G','T','A','C']

def matconfc1(virus):
    bd={}
    prob=np.zeros((4,4))
    for i in range(len(virus)-1): 
        bd[virus[i]]=[] 
        
    for i in range(len(virus)-1): 
        bd[virus[i]].append(virus[i+1])
        
    for i in range(len(bases)):
        for j in range(len(bases)):
            prob[i,j]=bd[bases[i]].count(bases[j])/len(bd[bases[i]])
       
    return prob